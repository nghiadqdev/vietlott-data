# 🔮 Tóm tắt Dự đoán Vietlott Power 645

> **Được tạo**: 2026-03-20 22:11:16
> **Seed**: 42 (deterministic), **Seed runs**: 3
>
>
> Tài liệu này chứa các dự đoán học máy cho dữ liệu xổ số Việt Nam.
> Đây là một mô-đun thử nghiệm chỉ dành cho mục đích giáo dục.

## 📊 So sánh Hiệu suất Chiến lược

> Sắp xếp theo ROI (tốt nhất → tệ nhất). Tất cả các chiến lược được kiểm thử với **20 vé/lần quay**.
> Lưu ý: Tất cả ROI đều âm sâu — xác suất xổ số khiến lợi nhuận không thể xảy ra ở quy mô lớn.
> So sánh cho thấy *chiến lược nào thua ít nhất*, không phải chiến lược nào có lợi.

| Hạng | Chiến lược | Tổng Chi phí (tr) | Tổng Lợi nhuận (tr) | Lợi nhuận ròng (tr) | ROI |
|------|----------|-----------------|-----------------|-----------------|-----|
| 🥇 1 | Chiến lược Suy giảm Exponential | 297tr | 10,058tr | 9,761tr | 3286.53% |
| 🥈 2 | Chiến lược Số Nóng | 297tr | 5,052.4tr | 4,755.4tr | 1601.13% |
| 🥉 3 | Chiến lược Số Lạnh | 297tr | 5,051.9tr | 4,754.9tr | 1600.98% |
|    4 | Chiến lược Vắng mặt Lâu dài | 297tr | 5,050.8tr | 4,753.8tr | 1600.61% |
|    5 | Chiến lược Không Lặp lại | 297tr | 58.4tr | -238.7tr | -80.35% |
|    6 | Chiến lược Mẫu | 297tr | 58.1tr | -238.9tr | -80.44% |
|    7 | Chiến lược Tần suất Cặp | 297tr | 56.6tr | -240.3tr | -80.93% |
|    8 | Chiến lược Ngẫu nhiên | 297tr | 50.9tr | -246.2tr | -82.88% |


## 📊 So sánh ROI: Benchmark vs Khung nhớ động

> Bảng A là benchmark cố định trên toàn bộ lịch sử.
> Bảng B là ROI ở cửa sổ gần đây **120 kỳ quay gần nhất** để mô phỏng vận hành động.
> Cột **ΔROI** giúp bạn thấy mức thay đổi khi chuyển từ khung nhớ cố định sang khung nhớ gần.

### Bảng A: ROI Benchmark (Toàn kỳ)

| Hạng | Chiến lược | Tổng Chi phí (tr) | Tổng Lợi nhuận (tr) | Lợi nhuận ròng (tr) | ROI Toàn kỳ |
|------|------------|-------------------|---------------------|---------------------|-------------|
| 🥇 1 | Chiến lược Suy giảm Exponential | 297tr | 10,058tr | 9,761tr | 3286.53% |
| 🥈 2 | Chiến lược Số Nóng | 297tr | 5,052.4tr | 4,755.4tr | 1601.13% |
| 🥉 3 | Chiến lược Số Lạnh | 297tr | 5,051.9tr | 4,754.9tr | 1600.98% |
|    4 | Chiến lược Vắng mặt Lâu dài | 297tr | 5,050.8tr | 4,753.8tr | 1600.61% |
|    5 | Chiến lược Không Lặp lại | 297tr | 58.4tr | -238.7tr | -80.35% |
|    6 | Chiến lược Mẫu | 297tr | 58.1tr | -238.9tr | -80.44% |
|    7 | Chiến lược Tần suất Cặp | 297tr | 56.6tr | -240.3tr | -80.93% |
|    8 | Chiến lược Ngẫu nhiên | 297tr | 50.9tr | -246.2tr | -82.88% |

### Bảng B: ROI Khung nhớ động (OOS gần đây)

| Hạng | Chiến lược | Chi phí OOS (tr) | Lợi nhuận OOS (tr) | ROI OOS | ΔROI (OOS - Toàn kỳ) |
|------|------------|------------------|--------------------|---------|-----------------------|
| 🥇 1 | Chiến lược Số Lạnh | 24tr | 5,004.4tr | 20751.46% | +19150.48% |
| 🥈 2 | Chiến lược Không Lặp lại | 24tr | 11.7tr | -51.25% | +29.10% |
| 🥉 3 | Chiến lược Mẫu | 24tr | 5.7tr | -76.25% | +4.19% |
|    4 | Chiến lược Số Nóng | 24tr | 5.2tr | -78.33% | -1679.46% |
|    5 | Chiến lược Tần suất Cặp | 24tr | 4.7tr | -80.42% | +0.51% |
|    6 | Chiến lược Suy giảm Exponential | 24tr | 4.2tr | -82.50% | -3369.03% |
|    7 | Chiến lược Vắng mặt Lâu dài | 24tr | 4.2tr | -82.71% | -1683.31% |
|    8 | Chiến lược Ngẫu nhiên | 24tr | 3tr | -87.29% | -4.41% |


## 📉 Biểu đồ ROI Tổng quát

> Biểu đồ thanh tương đối để nhìn nhanh chiến lược nào đang trội/yếu trong lần chạy hiện tại.
> Dấu '+' là ROI dương, dấu '-' là ROI âm. Độ dài thanh được chuẩn hóa theo giá trị tuyệt đối lớn nhất.

| Chiến lược | ROI | Biểu đồ tương đối |
|------------|-----|-------------------|
| Chiến lược Suy giảm Exponential | 3286.53% | ++++++++++++++++++++++++ |
| Chiến lược Số Nóng | 1601.13% | +++++++++++ |
| Chiến lược Số Lạnh | 1600.98% | +++++++++++ |
| Chiến lược Vắng mặt Lâu dài | 1600.61% | +++++++++++ |
| Chiến lược Không Lặp lại | -80.35% | - |
| Chiến lược Mẫu | -80.44% | - |
| Chiến lược Tần suất Cặp | -80.93% | - |
| Chiến lược Ngẫu nhiên | -82.88% | - |


## 📋 Bảng Chiến lược Tóm tắt

> Ngày dự đoán: **2026-03-20**.
> Dạng tóm tắt: Cấu hình, Kỳ Kiểm thử, Tóm tắt Tài chính, Phân bố Trùng khớp, KQ nổi bật (>=5 số trùng), 6 Hàng đầu.

| Chiến lược | Cấu hình | Kỳ Kiểm thử | Tóm tắt Tài chính | Phân bố Trùng khớp | KQ nổi bật (>=5) | 6 Hàng đầu |
|----------|---------------|-----------------|-------------------|--------------------|--------------|--------|
| Chiến lược Suy giảm Exponential | dải 1-45, chọn 6, vé/ngày 20 | 2016-07-20 00:00:00 → 2026-03-18 00:00:00 (1,485 lần quay/29,700 dự đoán) | chi 297tr, lợi 10,058tr, roi 3286.53% | 5+: 2, 4: 49, 3: 670 | 2 hàng với >=5 số trùng | 42, 36, 23, 45, 31, 28 |
| Chiến lược Số Nóng | dải 1-45, chọn 6, vé/ngày 20 | 2016-07-20 00:00:00 → 2026-03-18 00:00:00 (1,485 lần quay/29,700 dự đoán) | chi 297tr, lợi 5,052.4tr, roi 1601.13% | 5+: 1, 4: 44, 3: 607 | 1 hàng với >=5 số trùng | 28, 24, 17, 30, 32, 42 |
| Chiến lược Số Lạnh | dải 1-45, chọn 6, vé/ngày 20 | 2016-07-20 00:00:00 → 2026-03-18 00:00:00 (1,485 lần quay/29,700 dự đoán) | chi 297tr, lợi 5,051.9tr, roi 1600.98% | 5+: 1, 4: 36, 3: 678 | 1 hàng với >=5 số trùng | 27, 33, 3, 19, 38, 35 |
| Chiến lược Vắng mặt Lâu dài | dải 1-45, chọn 6, vé/ngày 20 | 2016-07-20 00:00:00 → 2026-03-18 00:00:00 (1,485 lần quay/29,700 dự đoán) | chi 297tr, lợi 5,050.8tr, roi 1600.61% | 5+: 1, 4: 41, 3: 606 | 1 hàng với >=5 số trùng | 43, 41, 40, 24, 27, 29 |
| Chiến lược Không Lặp lại | dải 1-45, chọn 6, vé/ngày 20 | 2016-07-20 00:00:00 → 2026-03-18 00:00:00 (1,485 lần quay/29,700 dự đoán) | chi 297tr, lợi 58.4tr, roi -80.35% | 5+: 0, 4: 59, 3: 577 | 0 hàng với >=5 số trùng | 39, 43, 27, 41, 3, 30 |
| Chiến lược Mẫu | dải 1-45, chọn 6, vé/ngày 20 | 2016-07-20 00:00:00 → 2026-03-18 00:00:00 (1,485 lần quay/29,700 dự đoán) | chi 297tr, lợi 58.1tr, roi -80.44% | 5+: 0, 4: 47, 3: 692 | 0 hàng với >=5 số trùng | 8, 20, 27, 31, 35, 32 |
| Chiến lược Tần suất Cặp | dải 1-45, chọn 6, vé/ngày 20 | 2016-07-20 00:00:00 → 2026-03-18 00:00:00 (1,485 lần quay/29,700 dự đoán) | chi 297tr, lợi 56.6tr, roi -80.93% | 5+: 0, 4: 49, 3: 643 | 0 hàng với >=5 số trùng | 42, 7, 28, 31, 43, 23 |
| Chiến lược Ngẫu nhiên | dải 1-45, chọn 6, vé/ngày 20 | 2016-07-20 00:00:00 → 2026-03-18 00:00:00 (1,485 lần quay/29,700 dự đoán) | chi 297tr, lợi 50.9tr, roi -82.88% | 5+: 0, 4: 37, 3: 647 | 0 hàng với >=5 số trùng | 6, 1, 23, 22, 28, 12 |


## 🔭 Dự đoán Số cho Lần Quay Tiếp theo

> Dự đoán cho lần quay tiếp theo vào: **2026-03-20**.
> Phương pháp: mỗi chiến lược mô phỏng **200** vé, sau đó tất cả vé được tổng hợp.
> Đây là xếp hạng xác suất, không phải các số trúng đảm bảo.

### 6 số ứng cử viên hàng đầu (tập hợp)

| Số | Điểm Tập hợp | Xuất hiện trong Vé |
|--------|----------------|---------------------|
| 5 | 433 | 27.06% |
| 3 | 413 | 25.81% |
| 43 | 413 | 25.81% |
| 41 | 408 | 25.50% |
| 30 | 404 | 25.25% |
| 27 | 400 | 25.00% |

### 6 hàng đầu theo Chiến lược

| Chiến lược | Số hàng đầu |
|----------|-------------|
| Chiến lược Suy giảm Exponential | 44, 1, 31, 6, 7, 43 |
| Chiến lược Số Nóng | 23, 31, 21, 28, 32, 36 |
| Chiến lược Số Lạnh | 15, 11, 10, 40, 6, 33 |
| Chiến lược Vắng mặt Lâu dài | 5, 27, 41, 30, 38, 39 |
| Chiến lược Không Lặp lại | 3, 41, 43, 39, 27, 30 |
| Chiến lược Mẫu | 13, 35, 14, 7, 18, 4 |
| Chiến lược Tần suất Cặp | 28, 9, 44, 7, 45, 42 |
| Chiến lược Ngẫu nhiên | 20, 35, 42, 15, 40, 11 |


## 🧪 Đánh giá Rolling Out-of-Sample

> Cửa sổ kiểm thử ngoài mẫu: **120 kỳ quay gần nhất** (đến 2026-03-18).
> Mục tiêu: đánh giá chiến lược trên giai đoạn gần đây, giảm thiên lệch do fit vào toàn bộ lịch sử.

| Chiến lược | Giai đoạn OOS | Tài chính OOS | Phân bố trùng khớp OOS |
|------------|----------------|---------------|--------------------------|
| Chiến lược Số Lạnh | 2025-06-13 00:00:00 → 2026-03-18 00:00:00 (2,400 dự đoán) | chi 24tr, lợi 5,004.4tr, roi 20751.46% | 6+: 0, 5: 1, 4: 3, 3: 57 |
| Chiến lược Không Lặp lại | 2025-06-13 00:00:00 → 2026-03-18 00:00:00 (2,400 dự đoán) | chi 24tr, lợi 11.7tr, roi -51.25% | 6+: 0, 5: 0, 4: 21, 3: 24 |
| Chiến lược Mẫu | 2025-06-13 00:00:00 → 2026-03-18 00:00:00 (2,400 dự đoán) | chi 24tr, lợi 5.7tr, roi -76.25% | 6+: 0, 5: 0, 4: 6, 3: 54 |
| Chiến lược Số Nóng | 2025-06-13 00:00:00 → 2026-03-18 00:00:00 (2,400 dự đoán) | chi 24tr, lợi 5.2tr, roi -78.33% | 6+: 0, 5: 0, 4: 5, 3: 54 |
| Chiến lược Tần suất Cặp | 2025-06-13 00:00:00 → 2026-03-18 00:00:00 (2,400 dự đoán) | chi 24tr, lợi 4.7tr, roi -80.42% | 6+: 0, 5: 0, 4: 5, 3: 44 |
| Chiến lược Suy giảm Exponential | 2025-06-13 00:00:00 → 2026-03-18 00:00:00 (2,400 dự đoán) | chi 24tr, lợi 4.2tr, roi -82.50% | 6+: 0, 5: 0, 4: 4, 3: 44 |
| Chiến lược Vắng mặt Lâu dài | 2025-06-13 00:00:00 → 2026-03-18 00:00:00 (2,400 dự đoán) | chi 24tr, lợi 4.2tr, roi -82.71% | 6+: 0, 5: 0, 4: 3, 3: 53 |
| Chiến lược Ngẫu nhiên | 2025-06-13 00:00:00 → 2026-03-18 00:00:00 (2,400 dự đoán) | chi 24tr, lợi 3tr, roi -87.29% | 6+: 0, 5: 0, 4: 1, 3: 51 |


## 📈 Độ ổn định Nhiều Seed

> Bảng dưới tổng hợp kết quả qua **3 lần chạy seed**.
> Ưu tiên chiến lược có ROI trung bình cao và độ lệch chuẩn thấp.

| Chiến lược | ROI TB | ROI Độ lệch chuẩn | Lợi nhuận TB (tr) | Lợi nhuận Độ lệch chuẩn (tr) |
|------------|--------|-------------------|--------------------|--------------------------|
| Chiến lược Ngẫu nhiên | 2723.51% | 2100.09% | 8,088.8tr | 6,237.3tr |
| Chiến lược Suy giảm Exponential | 1602.26% | 1374.83% | 4,758.7tr | 4,083.2tr |
| Chiến lược Mẫu | 1602.25% | 1373.87% | 4,758.7tr | 4,080.4tr |
| Chiến lược Số Lạnh | 1601.96% | 1374.02% | 4,757.8tr | 4,080.9tr |
| Chiến lược Số Nóng | 1039.91% | 793.46% | 3,088.5tr | 2,356.6tr |
| Chiến lược Vắng mặt Lâu dài | 1039.26% | 793.53% | 3,086.6tr | 2,356.8tr |
| Chiến lược Tần suất Cặp | 479.61% | 793.16% | 1,424.5tr | 2,355.7tr |
| Chiến lược Không Lặp lại | -79.57% | 0.55% | -236.3tr | 1.6tr |


## 🧾 Leaderboard Lịch sử

> Tổng hợp từ **7 bản ghi gần nhất** của sản phẩm `power_645`.
> Bảng này giúp ưu tiên chiến lược ổn định theo thời gian, không chỉ theo một lần chạy.

| Hạng | Chiến lược | ROI TB lịch sử | ROI Độ lệch chuẩn | Số run |
|------|------------|----------------|-------------------|--------|
| 1 | Chiến lược Ngẫu nhiên | 2723.51% | 2100.09% | 21 |
| 2 | Chiến lược Suy giảm Exponential | 1602.26% | 1374.83% | 21 |
| 3 | Chiến lược Mẫu | 1602.25% | 1373.87% | 21 |
| 4 | Chiến lược Số Lạnh | 1601.96% | 1374.02% | 21 |
| 5 | Chiến lược Số Nóng | 1039.91% | 793.46% | 21 |
| 6 | Chiến lược Vắng mặt Lâu dài | 1039.26% | 793.53% | 21 |
| 7 | Chiến lược Tần suất Cặp | 479.61% | 793.16% | 21 |
| 8 | Chiến lược Không Lặp lại | -79.57% | 0.55% | 21 |


---

## ⚠️ Tuyên bố Miễn trách nhiệm

Tóm tắt dự đoán này chỉ dành cho mục đích giáo dục và nghiên cứu. Kết quả xổ số ngẫu nhiên và không thể dự đoán một cách đáng tin cậy. Không bao giờ cờ bạc nhiều hơn những gì bạn có thể mất được.
