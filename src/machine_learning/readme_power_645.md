# 🔮 Tóm tắt Dự đoán Vietlott Power 645

> **Được tạo**: 2026-03-21 22:05:02
> **Seed**: ngẫu nhiên, **Seed runs**: 1
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
| 🥇 1 | Chiến lược Vắng mặt Lâu dài | 297.2tr | 10,050.6tr | 9,753.5tr | 3281.78% |
| 🥈 2 | Chiến lược Số Nóng | 297.2tr | 5,061.4tr | 4,764.2tr | 1603.03% |
| 🥉 3 | Chiến lược Suy giảm Exponential | 297.2tr | 5,055.4tr | 4,758.2tr | 1601.03% |
|    4 | Chiến lược Mẫu | 297.2tr | 5,055.3tr | 4,758.1tr | 1600.98% |
|    5 | Chiến lược Số Lạnh | 297.2tr | 5,049.5tr | 4,752.3tr | 1599.02% |
|    6 | Chiến lược Không Lặp lại | 297.2tr | 58tr | -239.2tr | -80.48% |
|    7 | Chiến lược Tần suất Cặp | 297.2tr | 55.5tr | -241.7tr | -81.33% |
|    8 | Chiến lược Ngẫu nhiên | 297.2tr | 52.1tr | -245.1tr | -82.47% |


## 📊 So sánh ROI: Benchmark vs Khung nhớ động

> Bảng A là benchmark cố định trên toàn bộ lịch sử.
> Bảng B là ROI ở cửa sổ gần đây **365 ngày gần nhất** để mô phỏng vận hành động.
> Cột **ΔROI** giúp bạn thấy mức thay đổi khi chuyển từ khung nhớ cố định sang khung nhớ gần.

### Bảng A: ROI Benchmark (Toàn kỳ)

| Hạng | Chiến lược | Tổng Chi phí (tr) | Tổng Lợi nhuận (tr) | Lợi nhuận ròng (tr) | ROI Toàn kỳ |
|------|------------|-------------------|---------------------|---------------------|-------------|
| 🥇 1 | Chiến lược Vắng mặt Lâu dài | 297.2tr | 10,050.6tr | 9,753.5tr | 3281.78% |
| 🥈 2 | Chiến lược Số Nóng | 297.2tr | 5,061.4tr | 4,764.2tr | 1603.03% |
| 🥉 3 | Chiến lược Suy giảm Exponential | 297.2tr | 5,055.4tr | 4,758.2tr | 1601.03% |
|    4 | Chiến lược Mẫu | 297.2tr | 5,055.3tr | 4,758.1tr | 1600.98% |
|    5 | Chiến lược Số Lạnh | 297.2tr | 5,049.5tr | 4,752.3tr | 1599.02% |
|    6 | Chiến lược Không Lặp lại | 297.2tr | 58tr | -239.2tr | -80.48% |
|    7 | Chiến lược Tần suất Cặp | 297.2tr | 55.5tr | -241.7tr | -81.33% |
|    8 | Chiến lược Ngẫu nhiên | 297.2tr | 52.1tr | -245.1tr | -82.47% |

### Bảng B: ROI Khung nhớ động (OOS gần đây)

| Hạng | Chiến lược | Chi phí OOS (tr) | Lợi nhuận OOS (tr) | ROI OOS | ΔROI (OOS - Toàn kỳ) |
|------|------------|------------------|--------------------|---------|-----------------------|
| 🥇 1 | Chiến lược Không Lặp lại | 31.4tr | 12.8tr | -59.39% | +21.09% |
| 🥈 2 | Chiến lược Số Nóng | 31.4tr | 8.7tr | -72.29% | -1675.32% |
| 🥉 3 | Chiến lược Tần suất Cặp | 31.4tr | 8.4tr | -73.09% | +8.24% |
|    4 | Chiến lược Suy giảm Exponential | 31.4tr | 6.2tr | -80.10% | -1681.12% |
|    5 | Chiến lược Mẫu | 31.4tr | 5.8tr | -81.69% | -1682.66% |
|    6 | Chiến lược Ngẫu nhiên | 31.4tr | 5.5tr | -82.32% | +0.14% |
|    7 | Chiến lược Vắng mặt Lâu dài | 31.4tr | 5.2tr | -83.44% | -3365.22% |
|    8 | Chiến lược Số Lạnh | 31.4tr | 5tr | -84.08% | -1683.10% |


## 📉 Biểu đồ ROI Tổng quát

> Biểu đồ thanh tương đối để nhìn nhanh chiến lược nào đang trội/yếu trong lần chạy hiện tại.
> Dấu '+' là ROI dương, dấu '-' là ROI âm. Độ dài thanh được chuẩn hóa theo giá trị tuyệt đối lớn nhất.

| Chiến lược | ROI | Biểu đồ tương đối |
|------------|-----|-------------------|
| Chiến lược Vắng mặt Lâu dài | 3281.78% | ++++++++++++++++++++++++ |
| Chiến lược Số Nóng | 1603.03% | +++++++++++ |
| Chiến lược Suy giảm Exponential | 1601.03% | +++++++++++ |
| Chiến lược Mẫu | 1600.98% | +++++++++++ |
| Chiến lược Số Lạnh | 1599.02% | +++++++++++ |
| Chiến lược Không Lặp lại | -80.48% | - |
| Chiến lược Tần suất Cặp | -81.33% | - |
| Chiến lược Ngẫu nhiên | -82.47% | - |


## 📋 Bảng Chiến lược Tóm tắt

> Ngày dự đoán: **2026-03-22**.
> Dạng tóm tắt: Cấu hình, Kỳ Kiểm thử, Tóm tắt Tài chính, Phân bố Trùng khớp, KQ nổi bật (>=5 số trùng), 6 Hàng đầu.

| Chiến lược | Cấu hình | Kỳ Kiểm thử | Tóm tắt Tài chính | Phân bố Trùng khớp | KQ nổi bật (>=5) | 6 Hàng đầu |
|----------|---------------|-----------------|-------------------|--------------------|--------------|--------|
| Chiến lược Vắng mặt Lâu dài | dải 1-45, chọn 6, vé/ngày 20 | 2016-07-20 00:00:00 → 2026-03-20 00:00:00 (1,486 lần quay/29,720 dự đoán) | chi 297.2tr, lợi 10,050.6tr, roi 3281.78% | 5+: 2, 4: 38, 3: 633 | 2 hàng với >=5 số trùng | 29, 39, 27, 3, 17, 45 |
| Chiến lược Số Nóng | dải 1-45, chọn 6, vé/ngày 20 | 2016-07-20 00:00:00 → 2026-03-20 00:00:00 (1,486 lần quay/29,720 dự đoán) | chi 297.2tr, lợi 5,061.4tr, roi 1603.03% | 5+: 1, 4: 58, 3: 648 | 1 hàng với >=5 số trùng | 5, 23, 43, 36, 30, 29 |
| Chiến lược Suy giảm Exponential | dải 1-45, chọn 6, vé/ngày 20 | 2016-07-20 00:00:00 → 2026-03-20 00:00:00 (1,486 lần quay/29,720 dự đoán) | chi 297.2tr, lợi 5,055.4tr, roi 1601.03% | 5+: 1, 4: 45, 3: 659 | 1 hàng với >=5 số trùng | 22, 23, 43, 28, 38, 2 |
| Chiến lược Mẫu | dải 1-45, chọn 6, vé/ngày 20 | 2016-07-20 00:00:00 → 2026-03-20 00:00:00 (1,486 lần quay/29,720 dự đoán) | chi 297.2tr, lợi 5,055.3tr, roi 1600.98% | 5+: 1, 4: 48, 3: 626 | 1 hàng với >=5 số trùng | 9, 7, 12, 37, 8, 4 |
| Chiến lược Số Lạnh | dải 1-45, chọn 6, vé/ngày 20 | 2016-07-20 00:00:00 → 2026-03-20 00:00:00 (1,486 lần quay/29,720 dự đoán) | chi 297.2tr, lợi 5,049.5tr, roi 1599.02% | 5+: 1, 4: 35, 3: 640 | 1 hàng với >=5 số trùng | 25, 12, 33, 40, 17, 14 |
| Chiến lược Không Lặp lại | dải 1-45, chọn 6, vé/ngày 20 | 2016-07-20 00:00:00 → 2026-03-20 00:00:00 (1,486 lần quay/29,720 dự đoán) | chi 297.2tr, lợi 58tr, roi -80.48% | 5+: 0, 4: 60, 3: 560 | 0 hàng với >=5 số trùng | 3, 5, 27, 30, 39, 41 |
| Chiến lược Tần suất Cặp | dải 1-45, chọn 6, vé/ngày 20 | 2016-07-20 00:00:00 → 2026-03-20 00:00:00 (1,486 lần quay/29,720 dự đoán) | chi 297.2tr, lợi 55.5tr, roi -81.33% | 5+: 0, 4: 41, 3: 700 | 0 hàng với >=5 số trùng | 31, 7, 23, 29, 44, 43 |
| Chiến lược Ngẫu nhiên | dải 1-45, chọn 6, vé/ngày 20 | 2016-07-20 00:00:00 → 2026-03-20 00:00:00 (1,486 lần quay/29,720 dự đoán) | chi 297.2tr, lợi 52.1tr, roi -82.47% | 5+: 0, 4: 43, 3: 612 | 0 hàng với >=5 số trùng | 29, 33, 31, 27, 16, 7 |


## 🔭 Dự đoán Số cho Lần Quay Tiếp theo

> Dự đoán cho lần quay tiếp theo vào: **2026-03-22**.
> Phương pháp: mỗi chiến lược mô phỏng **200** vé, sau đó tất cả vé được tổng hợp.
> Đây là xếp hạng xác suất, không phải các số trúng đảm bảo.

### Bảng A - 6 số ứng cử viên theo Toàn kỳ

| Số | Điểm Tập hợp | Xuất hiện trong Vé |
|--------|----------------|---------------------|
| 30 | 462 | 28.88% |
| 39 | 452 | 28.25% |
| 3 | 432 | 27.00% |
| 41 | 432 | 27.00% |
| 27 | 427 | 26.69% |
| 5 | 418 | 26.12% |

### Bảng B - 6 số ứng cử viên theo Khung nhớ động

> Trọng số chiến lược được tính theo ROI OOS trong **365 ngày gần nhất**.

| Số | Điểm Động (weighted) | Tỷ trọng Điểm Động |
|--------|-----------------------|--------------------|
| 30 | 462.0 | 4.81% |
| 39 | 452.0 | 4.71% |
| 3 | 432.0 | 4.50% |
| 41 | 432.0 | 4.50% |
| 27 | 427.0 | 4.45% |
| 5 | 418.0 | 4.35% |

### 6 hàng đầu theo Chiến lược - Bảng A (xếp theo ROI Toàn kỳ)

| Chiến lược | Số hàng đầu |
|----------|-------------|
| Chiến lược Vắng mặt Lâu dài | 39, 30, 29, 17, 15, 1 |
| Chiến lược Số Nóng | 45, 42, 31, 28, 20, 12 |
| Chiến lược Suy giảm Exponential | 42, 31, 28, 7, 2, 1 |
| Chiến lược Mẫu | 30, 23, 6, 4, 3, 2 |
| Chiến lược Số Lạnh | 41, 40, 33, 25, 18, 3 |
| Chiến lược Không Lặp lại | 41, 39, 30, 27, 5, 3 |
| Chiến lược Tần suất Cặp | 45, 43, 42, 28, 22, 17 |
| Chiến lược Ngẫu nhiên | 42, 41, 39, 35, 26, 2 |

### 6 hàng đầu theo Chiến lược - Bảng B (xếp theo ROI Khung nhớ động)

> Xếp hạng theo ROI OOS trong **365 ngày gần nhất**.

| Chiến lược | Số hàng đầu |
|----------|-------------|
| Chiến lược Không Lặp lại | 41, 39, 30, 27, 5, 3 |
| Chiến lược Số Nóng | 45, 42, 31, 28, 20, 12 |
| Chiến lược Tần suất Cặp | 45, 43, 42, 28, 22, 17 |
| Chiến lược Suy giảm Exponential | 42, 31, 28, 7, 2, 1 |
| Chiến lược Mẫu | 30, 23, 6, 4, 3, 2 |
| Chiến lược Ngẫu nhiên | 42, 41, 39, 35, 26, 2 |
| Chiến lược Vắng mặt Lâu dài | 39, 30, 29, 17, 15, 1 |
| Chiến lược Số Lạnh | 41, 40, 33, 25, 18, 3 |


## 🧪 Đánh giá Rolling Out-of-Sample

> Cửa sổ kiểm thử ngoài mẫu: **365 ngày gần nhất** (đến 2026-03-20).
> Mục tiêu: đánh giá chiến lược trên giai đoạn gần đây, giảm thiên lệch do fit vào toàn bộ lịch sử.

| Chiến lược | Giai đoạn OOS | Tài chính OOS | Phân bố trùng khớp OOS |
|------------|----------------|---------------|--------------------------|
| Chiến lược Không Lặp lại | 2025-03-21 00:00:00 → 2026-03-20 00:00:00 (3,140 dự đoán) | chi 31.4tr, lợi 12.8tr, roi -59.39% | 6+: 0, 5: 0, 4: 21, 3: 45 |
| Chiến lược Số Nóng | 2025-03-21 00:00:00 → 2026-03-20 00:00:00 (3,140 dự đoán) | chi 31.4tr, lợi 8.7tr, roi -72.29% | 6+: 0, 5: 0, 4: 11, 3: 64 |
| Chiến lược Tần suất Cặp | 2025-03-21 00:00:00 → 2026-03-20 00:00:00 (3,140 dự đoán) | chi 31.4tr, lợi 8.4tr, roi -73.09% | 6+: 0, 5: 0, 4: 8, 3: 89 |
| Chiến lược Suy giảm Exponential | 2025-03-21 00:00:00 → 2026-03-20 00:00:00 (3,140 dự đoán) | chi 31.4tr, lợi 6.2tr, roi -80.10% | 6+: 0, 5: 0, 4: 6, 3: 65 |
| Chiến lược Mẫu | 2025-03-21 00:00:00 → 2026-03-20 00:00:00 (3,140 dự đoán) | chi 31.4tr, lợi 5.8tr, roi -81.69% | 6+: 0, 5: 0, 4: 5, 3: 65 |
| Chiến lược Ngẫu nhiên | 2025-03-21 00:00:00 → 2026-03-20 00:00:00 (3,140 dự đoán) | chi 31.4tr, lợi 5.5tr, roi -82.32% | 6+: 0, 5: 0, 4: 4, 3: 71 |
| Chiến lược Vắng mặt Lâu dài | 2025-03-21 00:00:00 → 2026-03-20 00:00:00 (3,140 dự đoán) | chi 31.4tr, lợi 5.2tr, roi -83.44% | 6+: 0, 5: 0, 4: 3, 3: 74 |
| Chiến lược Số Lạnh | 2025-03-21 00:00:00 → 2026-03-20 00:00:00 (3,140 dự đoán) | chi 31.4tr, lợi 5tr, roi -84.08% | 6+: 0, 5: 0, 4: 4, 3: 60 |




## 🧾 Leaderboard Lịch sử

> Tổng hợp từ **12 bản ghi gần nhất** của sản phẩm `power_645`.
> Bảng này giúp ưu tiên chiến lược ổn định theo thời gian, không chỉ theo một lần chạy.

| Hạng | Chiến lược | ROI TB lịch sử | ROI Độ lệch chuẩn | Số run |
|------|------------|----------------|-------------------|--------|
| 1 | Chiến lược Ngẫu nhiên | 2640.99% | 2122.59% | 34 |
| 2 | Chiến lược Suy giảm Exponential | 1651.65% | 1383.85% | 34 |
| 3 | Chiến lược Mẫu | 1602.17% | 1353.52% | 34 |
| 4 | Chiến lược Số Lạnh | 1552.47% | 1383.20% | 34 |
| 5 | Chiến lược Số Nóng | 1006.94% | 804.32% | 34 |
| 6 | Chiến lược Vắng mặt Lâu dài | 1006.30% | 804.37% | 34 |
| 7 | Chiến lược Tần suất Cặp | 463.10% | 787.15% | 34 |
| 8 | Chiến lược Không Lặp lại | -79.55% | 0.56% | 34 |


---

## ⚠️ Tuyên bố Miễn trách nhiệm

Tóm tắt dự đoán này chỉ dành cho mục đích giáo dục và nghiên cứu. Kết quả xổ số ngẫu nhiên và không thể dự đoán một cách đáng tin cậy. Không bao giờ cờ bạc nhiều hơn những gì bạn có thể mất được.
