# 🔮 Kiến trúc và Hoạt động Chi tiết của Vietlott ML App

## 📌 Phần I: Tổng quan về Hệ thống

### 1.1 Mục đích Chung
App là một **hệ thống dự đoán xổ số sử dụng Machine Learning** để phân tích dữ liệu lịch sử các kỳ quay của Vietlott. Nó chạy 8 chiến lược khác nhau để so sánh hiệu suất và tìm ra chiến lược có **ROI (Return on Investment) cao nhất**.

### 1.2 Luồng Công việc Chính

```
① Tải Dữ liệu
   └─> Đọc file JSONL từ /data/ (vd: power_645.jsonl)
   └─> Chứa toàn bộ lịch sử: ngày quay, số trúng thưởng

② Khởi tạo 8 Chiến lược
   └─> RandomModel (ngẫu nhiên)
   └─> FrequencyStrategy (tần suất cơ bản)
   └─> ExponentialDecayStrategy (tần suất với trọng số thời gian)
   └─> HotNumbersStrategy (số được quay nhiều - theo tần suất)
   └─> ColdNumbersStrategy (số hiếm được quay - theo tần suất)
   └─> LongAbsenceStrategy (số vắng mặt lâu)
   └─> NotRepeatStrategy (tránh số quay gần đây)
   └─> PatternStrategy (phân tích mẫu hình)
   └─> PairFrequencyStrategy (tần suất cặp số)

③ Backtest Lịch sử
   └─> Mỗi chiến lược dự đoán từng kỳ quay từ năm 2016 đến nay
   └─> So sánh dự đoán với kết quả thực
   └─> Tính số trúng khớp (3+, 4, 5, 6)
   └─> Ghi nhận chi phí (1 vé = mặc định 10,000 VND × dự đoán/ngày)

④ Tính Toán ROI
   └─> Chi phí = số vé dự đoán × 10,000 VND
   └─> Lợi nhuận = tổng thưởng nhận được
   └─> Lợi nhuận ròng = Lợi nhuận - Chi phí
   └─> ROI % = (Lợi nhuận ròng / Chi phí) × 100%

⑤ Đánh giá Out-of-Sample (OOS)
   └─> Chỉ lấy 120 kỳ quay gần nhất
   └─> Tính lại ROI trên giai đoạn này
   └─> Kiểm tra xem chiến lược có bị overfitting không

⑥ Chạy Multi-Seed
   └─> Chạy lại mỗi chiến lược với seed = 42, 43, 44
   └─> Tính ROI trung bình và độ lệch chuẩn
   └─> Biết được chiến lược nào ổn định nhất

⑦ Lưu Lịch sử
   └─> Ghi JSONL để tracking qua nhiều lần chạy
   └─> Xây dựng leaderboard dài hạn

⑧ Sinh Báo cáo
   └─> Markdown file (readme_power_645.md)
   └─> Chứa: bảng so sánh, dự đoán ngày hôm sau, OOS, ổn định multi-seed
```

### 1.3 Dữ liệu Input
- **File**: `/data/power_645.jsonl` (NDJSON format)
- **Mỗi dòng**: `{"date": "2026-03-20", "result": [5, 12, 23, 31, 42, 45]}`
- **Phạm vi**: 2016-07-20 → 2026-03-18 (≈1,485 kỳ quay)

### 1.4 Dữ liệu Output
- **Báo cáo**: `/src/machine_learning/readme_power_645.md` (Markdown)
- **Lịch sử**: `/src/machine_learning/prediction_run_history.jsonl` (JSONL)
- **Mỗi dòng lịch sử**: `{generated_at, product, seed, seed_runs, output_path, runs: [{...}, ...]}`

---

## 📌 Phần II: Nền tảng Chung - Lớp PredictModel

### 2.1 Kiến trúc Lớp Cơ sở

Tất cả 8 chiến lược đều kế thừa từ `PredictModel`. Lớp cơ sở này cung cấp:

```python
class PredictModel:
    def __init__(self, df: pd.DataFrame, time_predict: int = 1, 
                 min_val: int = 1, max_val: int = 45):
        """
        df: DataFrame lịch sử (có cột 'date' và 'result')
        time_predict: Số vé dự đoán mỗi ngày (mặc định 1, app dùng 20)
        min_val, max_val: Phạm vi số (1-45 cho Power 645)
        """
        self.df = df
        self.time_predict = time_predict  # 20 vé/ngày trong app
        self.number_predict = 6  # 6 số trong 1 vé
        self.min_val = min_val
        self.max_val = max_val
```

### 2.2 Quy trình 3 Bước Cơ bản

**Bước 1: `predict(target_date)` - Dự đoán Chiến lược**
- Mỗi chiến lược phải override method này
- Input: Ngày quay (vd: 2026-03-20)
- Output: 6 số dự đoán (vd: [5, 12, 23, 31, 42, 45])
- **Quy tắc**: Chỉ dùng dữ liệu TRƯỚC target_date (tránh look-ahead bias)

**Bước 2: `backtest()` - Kiểm tra Lịch sử**
```
Với mỗi ngày trong lịch sử:
  1. Gọi predict(ngày đó) → nhận 6 số dự đoán
  2. So sánh với kết quả thực tế → đếm trùng khớp
  3. Lưu kết quả: {predict_idx, predicted, correct, correct_num}

Kết quả lưu trong df_backtest (1,485 hàng, mỗi hàng 20 dự đoán)
```

**Bước 3: `evaluate()` + `revenue()` - Tính Hiệu suất**
```
Từ backtest kết quả:
  1. Đếm match distribution (6 trùng khớp, 5, 4, 3, v.v.)
  2. Tính tổng thưởng dựa trên bảng giải:
      6 trùng khớp: 10 tỷ VND (chia nhiều người)
      5 trùng khớp: 100 triệu VND (chia nhiều người)
      v.v...
  3. Chi phí = 1,485 ngày × 20 vé/ngày × 10,000 VND = 297 triệu
  4. ROI = (Lợi nhuận - Chi phí) / Chi phí × 100%
```

### 2.3 Tại sao ROI Đều Âm?

Đơn giản: **Lotto là ngành công nghiệp với odds định sẵn, nhà nước lấy ~30% mỗi vé.**

- Nếu mua 20 triệu vé hàng ngày 10 năm → mất ~297 tỷ VND
- Ngay cả chiến lược "tốt nhất" mua lại được ~10 tỷ
- ROI = (10 tỷ - 297 tỷ) / 297 tỷ = **-96.6%**

**Mục đích: Tìm chiến lược TỰA NHẤT (mất ít nhất), không phải có lợi.**

---

## 📌 Phần III: Ba Chiến lược Hàng đầu

### 3.1 🥇 Chiến lược Suy giảm Exponential (ExponentialDecayStrategy)

**ROI Toàn bộ**: **3286.53%** (lợi nhất)
**ROI OOS (120 ngày gần)**: -82.50% (tệ nhất OOS)
**Performance Multi-Seed**: ROI TB = 2723.51%, Độ lệch chuẩn = 2100.09% (không ổn định)

#### 🔍 Nguyên lý Hoạt động

```
Giả sử chúng ta dự đoán cho ngày 2026-03-20:

① Tính Điểm Số cho mỗi số từ 1-45
   ↓
   Mỗi kỳ quay lịch sử đóng góp một "điểm" 
   nhưng điểm THEO THỜI GIAN
   
   Công thức: w = exp(-ln(2) × ngày_cách_đó / 90)
   
   Ví dụ:
   - Ngày hôm qua (1 ngày cách): w ≈ 0.99 (gần 1, rất quan trọng)
   - 30 ngày trước:              w ≈ 0.57 (trung bình)
   - 90 ngày trước:              w = 0.50 (nửa)
   - 180 ngày trước:             w ≈ 0.25 (ít,gần như bỏ qua)
   - 1 năm trước:                w ≈ 0.04 (lăn ngoài)
   
② Gộp tất cả điểm
   Ví dụ: Số 5 xuất hiện trong 30 kỳ quay gần đây
   → điểm tổng = w₁ + w₂ + ... + w₃₀
   
③ Sắp xếp theo điểm cao→thấp (hot=True)
   Số 5: 15.2 điểm (cao)
   Số 7: 14.8 điểm
   ...
   Số 3: 2.1 điểm (thấp)
   
④ Chọn số từ "bể ngâm" có trọng số
   Tạo danh sách: [5, 5, 5, 5, ...(15 lần do có w cao), 7, 7, 7, 7, ..., 3, 3]
   
   Rút ngẫu nhiên 4.8 số (80% của 6 để có trọng số thay vì random)
   Ví dụ: [5, 7, 5, 23, 12] → bổ sung thêm 1 số random → [5, 7, 5, 23, 12, 41]
   
⑤ Trả lại [5, 7, 12, 23, 41, 45] (sắp xếp tăng)
```

#### 💡 Tại Sao Nó "Tốt Nhất"?

1. **Recency Bias (Sai lệch Gần Đây)**
   - Trọng số exponential → số được quay **gần đây** được ưu tiên
   - Nếu số 5 hot (được quay nhiều) trong 3 tháng gần → khả năng cao nó sẽ tiếp tục hot

2. **Không Hard Cutoff**
   - FrequencyStrategy dùng time_window cứng (365 ngày): nếu quá 365 ngày thì bỏ hết
   - ExponentialDecay: dùng tất cả lịch sử nhưng weighted → không có "cliff"

3. **Momentum Trading**
   - Gọi là "suy giảm có trọng số kỳ vọng"
   - Nắm bắt xu hướng ngắn hạn tốt hơn

#### ⚠️ Tuyệt Đối Không Chắc Chắn

- **OOS ROI = -82.50%**: Trên 120 ngày gần nhất, nó **TỆ HơN cả random**
- **Độ lệch chuẩn Multi-Seed = 2100%**: Seed 42 vs Seed 43 cho kết quả khác nhau RẤT NHIỀU
- **Kết luận**: Chiến lược này **vừa dở vừa không ổn định**, nhưng áp đặt đắn được vào cả bộ dữ liệu 10 năm

---

### 3.2 🥈 Chiến lược Số Nóng (HotNumbersStrategy)

**ROI Toàn bộ**: **1601.13%**
**ROI OOS (120 ngày gần)**: -78.33%
**Performance Multi-Seed**: Không có trong báo cáo hiện tại (chỉ có Random)

#### 🔍 Nguyên lý Hoạt động

```
Chiến lược đơn giản: Chọn các số được quay NHIỀU NHẤT
(theo logic: "nó hot không vì không có lý do" - phản ánh thực tại thống kê)

① Xác định Time Window: 365 ngày gần nhất
   
② Đếm Tần suất (Count Frequencies)
   Số 5: 45 lần xuất hiện trong 365 ngày
   Số 7: 42 lần
   Số 3: 8 lần
   ...

③ Sắp xếp từ cao→thấp
   5 (45), 7 (42), 23 (41), 31 (39), 12 (38), 45 (36), ...

④ Chọn từ "bể ngâm" có trọng số
   Tạo danh sách: [5, 5, ...(45 lần), 7, 7, ...(42 lần), 23, 23, ..., 31, 31, ...]
   
   Rút ngẫu nhiên 4.8 số (80% để trộn với random)
   Ví dụ: [5, 7, 5, 23, 31] → bổ sung 1 số random → [5, 7, 5, 23, 31, 44]

⑤ Trả lại sắp xếp: [5, 7, 23, 31, 44, ...]
```

#### 💡 Tại Sao Nó Hoạt Động?

1. **Thống kê Cơ bản**
   - Nếu 1,485 kỳ quay × 6 số/kỳ = 8,910 số được quay
   - Chia đều 45 chỉ có ≈198 lần mỗi số
   - Nhưng số 5: 45 × 1,485/365 ≈ 368/10 năm = 37 lần/năm
   - Nếu số 5 "hot" → nó lặp lại pattern này

2. **Giá Trị Trung bình Cao Hơn Random**
   - Random chọn ngẫu nhiên → xác suất mỗi số = 1/45
   - Hot chọn từ bể ngâm có trọng số → P(5) = 45/8910 ≈ 0.5% > 1/45 ≈ 2.2%
   - Nắm bắt được bias thống kê

#### ⚠️ Giới Hạn

- **Hard Cutoff 365 ngày**: Nếu số 5 rất hot 300 ngày qua nhưng biến cold, nó vẫn đc chọn
- **OOS ROI = -78.33%**: Tặc hơn Exponential trên 120 ngày mới
  - Gợi ý: pattern gần đây khác pattern lâu dài
  - Số được quay nhiều trước không nhất thiết được quay nhiều hiện tại

---

### 3.3 🥉 Chiến lược Số Lạnh (ColdNumbersStrategy)

**ROI Toàn bộ**: **1600.98%**
**ROI OOS (120 ngày gần)**: **20751.46%** ⭐ (TỐT NHẤT OOS!)
**Performance Multi-Seed**: Không có

#### 🔍 Nguyên lý Hoạt động

```
Chiến lược ngược lại: Chọn các số được quay ÍT NHẤT
(logic: "số này vắng lâu → cân bằng thống kê → sắp quay" - Mean Reversion)

① Time window: 365 ngày gần nhất

② Đếm Tần suất TỪNG SỐ
   Số 44: 5 lần (ÍT)
   Số 37: 8 lần
   Số 28: 15 lần
   Số 5: 45 lần (NHIỀU)

③ Sắp xếp từ thấp→cao (NGƯỢC với Hot)
   44 (5 lần), 37 (8 lần), 28 (15 lần), ..., 5 (45 lần)

④ Chọn từ bể ngâm có trọng số
   Trọng số = (max_frequency - current_frequency + 1)
   = (45 - 5 + 1) = 41 cho số 44
   = (45 - 8 + 1) = 38 cho số 37
   = (45 - 15 + 1) = 31 cho số 28
   
   Danh sách: [44, 44, ...(41 lần), 37, 37, ...(38 lần), ...]
   
   Rút ngẫu nhiên 4.8 số (80%)
   Ví dụ: [44, 37, 44, 28, 39] → +1 random → [28, 37, 39, 44, 44, ...]

⑤ Trả lại: [28, 37, 39, 44, ...]
```

#### 💡 Tại Sao Nó Hoạt Động? (Đặc Biệt trên OOS)

1. **Mean Reversion Phenomenon (Hiệu ứng Trở về Trung bình)**
   - Nếu số 44 không quay 3 tháng → thống kê nói nó sắp quay (để cân bằng)
   - Lô nhất định **không hoàn toàn random** → có quán tính ẩn

2. **OOS ROI = 20751% = TOP 1** ✨ 
   - Trên 120 ngày gần (2025-06-13 → 2026-03-18):
     - Số Lạnh: 1 lần match 5 số, 3 lần match 4 số, 57 lần match 3 số
     - Tổng thưởng: 5 tỷ / 24 triệu chi phí = **ROI cực cao**
   - Lý giải: Số ít được quay gần đây có xu hướng xuất hiện trong 1-2 tháng tới

3. **Ổn Định Hơn Hot trên mẫu Nhỏ**
   - Hot = phụ thuộc pattern lâu dài (10 năm)
   - Cold = phụ thuộc pattern gần đây (3-6 tháng)
   - Gần đây thường ổn định hơn lâu dài

#### ⚠️ Cẫn Thận

- **Variance Cao**: Ngày này match lớn, ngày khác 0 match
- **Có thể Overfitting**: ROI 20k% trên OOS có thể vì tình cờ (only 120 draws)
- **Multi-Seed Chưa Test**: Cần chạy seed khác để xác nhận stability

---

## 📌 Phần IV: So Sánh Ba Chiến lược

| Tiêu chí | Exponential | Hot Numbers | Cold Numbers |
|----------|-------------|-------------|--------------|
| **ROI Toàn bộ** | 3286.53% 🥇 | 1601.13% 🥈 | 1600.98% 🥉 |
| **ROI OOS (120d)** | -82.50% (tệ) | -78.33% | +20751% 🌟 |
| **Ổn định Multi-Seed** | 2723±2100% (rất bất ổn) | ? | ? |
| **Logic** | Recency + Exponential Weight | Tần suất cơ bản | Mean Reversion |
| **Kỳ vọng Lý thuyết** | Cao nhất | Trung bình | Thấp nhất toàn bộ |
| **Thực tế OOS** | Tệ nhất | Tệ | TỐT NHẤT |
| **Kết luận** | Overfitted rất nặng | Bình thường | **Underfitted, có upside** |

---

## 📌 Phần V: Cách Chạy và Các Tham số

### 5.1 Lệnh Cơ Bản

```bash
source .venv/bin/activate

# Chạy với seed cố định, 30 seeds khác nhau, xem 10 kỳ quay lịch sử OOS, 120 ngày gần
PYTHONPATH=src python src/machine_learning/render_prediction.py \
  --product power_645 \
  --seed 42 \
  --seed-runs 30 \
  --history-window 50 \
  --oos-draws 120
```

### 5.2 Các Tham số Chính

| Tham số | Ý nghĩa | Mặc định | Lời khuyên |
|---------|---------|---------|-----------|
| `--seed` | Seed RNG cố định | None (random mỗi lần) | Dùng 42 để reproducible |
| `--seed-runs` | Chạy N seeds (seed, seed+1, seed+2, ...) | 1 | Dùng 20-50 để giảm noise |
| `--history-window` | Lấy N record lịch sử gần nhất | 30 | Dùng 50 để trend dài hạn |
| `--oos-days` | OOS theo ngày (365 = 1 năm) | 365 | Thay bằng --oos-draws |
| `--oos-draws` | OOS theo số lần quay (120 = ~2 năm) | None | **DÙNG CÁI NÀY** |
| `--product` | Sản phẩm (power_645, power_655, v.v.) | power_645 | - |

### 5.3 Output Files

- **Báo cáo**: `src/machine_learning/readme_power_645.md`
  - Bảng so sánh hiệu suất
  - Dự đoán cho lần quay tới
  - OOS metrics
  - Stability (nếu seed-runs > 1)
  - History leaderboard (nếu lịch sử tồn tại)

- **Lịch sử**: `src/machine_learning/prediction_run_history.jsonl`
  - Một dòng JSON mỗi lần chạy
  - Chứa: timestamp, seed params, tất cả metrics

---

## 📌 Phần VI: Khuyến nghị Sử dụng

### 6.1 Để Tìm Chiến lược Tốt Nhất

```bash
# Chạy 1 lần với 30 seeds để giảm bruit
PYTHONPATH=src python src/machine_learning/render_prediction.py \
  --product power_645 \
  --seed 42 \
  --seed-runs 30 \
  --history-window 50 \
  --oos-draws 120
```

**Thứ tự ưu tiên khi chọn chiến lược:**
1. Xem **ROI OOS** → chiến lược nào cao nhất?
2. Xem **Stability** → ROI stddev thấp nhất?
3. **So sánh OOS ROI vs Toàn bộ ROI**:
   - Nếu OOS >> toàn bộ → chiến lược good tại vùng gần
   - Nếu OOS << toàn bộ → overfitted

### 6.2 Để Track Qua Thời Gian

Chạy mỗi tuần:
```bash
PYTHONPATH=src python src/machine_learning/render_prediction.py \
  --product power_645 \
  --seed 42 \
  --seed-runs 20 \
  --history-window 100 \
  --oos-draws 120
```

Xem **History Leaderboard** để biết:
- Chiến lược nào **liên tục** tốt?
- ROI trung bình qua 100 lần chạy?

### 6.3 Để Phát Hiện Overfitting

```
Nếu thấy:
- Toàn bộ ROI: +3000%
- OOS ROI: -80%

→ Chiến lược OVERFITTED NẶNG
→ Tránh dùng
```

---

## 🎯 Kết Luận

**3 Chiến lược Hàng đầu:**

1. **Chiến lược Suy giảm Exponential** 
   - 📊 Tốt nhất trên **toàn bộ lịch sử** (10 năm)
   - ❌ Nhưng **tệ nhất trên OOS** (120 ngày gần)
   - 📝 Kết luận: Chắt lọc pattern lâu dài, không còn hiệu lực hiện tại

2. **Chiến lược Số Nóng**
   - 📊 Bình thường trên toàn bộ (1600%)
   - ❌ Tệ trên OOS (-78%)
   - 📝 Sử dụng heuristic tần suất, nhưng thị trường thay đổi

3. **Chiến lược Số Lạnh**
   - 📊 Bình thường trên toàn bộ (1600%, giống Hot)
   - ✨ **TỐT NHẤT trên OOS** (+20k%)
   - 📝 Mean reversion tốt, nhưng có variance cao

**Đề xuất**: Nếu muốn chơi ngay tuần này, **dùng Số Lạnh**. Nếu study dài hạn, dùng kết hợp tất cả 3 để **phân tán rủi ro**.

