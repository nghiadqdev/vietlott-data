# 🔮 Tóm tắt Dự đoán Vietlott Power 645

> **Được tạo**: 2026-04-01 17:34:04
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
| 🥇 1 | Chiến lược Số Lạnh | 297.2tr | 10,059.8tr | 9,762.5tr | 3284.84% |
| 🥈 2 | Chiến lược Tần suất Cặp | 297.2tr | 10,054.9tr | 9,757.7tr | 3283.21% |
| 🥉 3 | Chiến lược Số Nóng | 297.2tr | 5,055.6tr | 4,758.4tr | 1601.06% |
|    4 | Chiến lược Suy giảm Exponential | 297.2tr | 5,051.7tr | 4,754.5tr | 1599.76% |
|    5 | Chiến lược Mẫu | 297.2tr | 5,050.7tr | 4,753.5tr | 1599.43% |
|    6 | Chiến lược Không Lặp lại | 297.2tr | 58.8tr | -238.4tr | -80.23% |
|    7 | Chiến lược Ngẫu nhiên | 297.2tr | 51tr | -246.2tr | -82.82% |
|    8 | Chiến lược Vắng mặt Lâu dài | 297.2tr | 45.1tr | -252.1tr | -84.81% |


## 📊 So sánh ROI: Benchmark vs Khung nhớ động

> Bảng A là benchmark cố định trên toàn bộ lịch sử.
> Bảng B là ROI ở cửa sổ gần đây **90 ngày gần nhất (tự động chọn)** để mô phỏng vận hành động.
> Cột **ΔROI** giúp bạn thấy mức thay đổi khi chuyển từ khung nhớ cố định sang khung nhớ gần.

### Bảng A: ROI Benchmark (Toàn kỳ)

| Hạng | Chiến lược | Tổng Chi phí (tr) | Tổng Lợi nhuận (tr) | Lợi nhuận ròng (tr) | ROI Toàn kỳ |
|------|------------|-------------------|---------------------|---------------------|-------------|
| 🥇 1 | Chiến lược Số Lạnh | 297.2tr | 10,059.8tr | 9,762.5tr | 3284.84% |
| 🥈 2 | Chiến lược Tần suất Cặp | 297.2tr | 10,054.9tr | 9,757.7tr | 3283.21% |
| 🥉 3 | Chiến lược Số Nóng | 297.2tr | 5,055.6tr | 4,758.4tr | 1601.06% |
|    4 | Chiến lược Suy giảm Exponential | 297.2tr | 5,051.7tr | 4,754.5tr | 1599.76% |
|    5 | Chiến lược Mẫu | 297.2tr | 5,050.7tr | 4,753.5tr | 1599.43% |
|    6 | Chiến lược Không Lặp lại | 297.2tr | 58.8tr | -238.4tr | -80.23% |
|    7 | Chiến lược Ngẫu nhiên | 297.2tr | 51tr | -246.2tr | -82.82% |
|    8 | Chiến lược Vắng mặt Lâu dài | 297.2tr | 45.1tr | -252.1tr | -84.81% |

### Bảng B: ROI Khung nhớ động (OOS gần đây)

| Hạng | Chiến lược | Chi phí OOS (tr) | Lợi nhuận OOS (tr) | ROI OOS | ΔROI (OOS - Toàn kỳ) |
|------|------------|------------------|--------------------|---------|-----------------------|
| 🥇 1 | Chiến lược Không Lặp lại | 7.8tr | 10.2tr | 30.13% | +110.36% |
| 🥈 2 | Chiến lược Số Lạnh | 7.8tr | 2.8tr | -64.10% | -3348.94% |
| 🥉 3 | Chiến lược Số Nóng | 7.8tr | 1.7tr | -78.21% | -1679.27% |
|    4 | Chiến lược Suy giảm Exponential | 7.8tr | 1.6tr | -80.13% | -1679.89% |
|    5 | Chiến lược Vắng mặt Lâu dài | 7.8tr | 1.3tr | -83.33% | +1.47% |
|    6 | Chiến lược Mẫu | 7.8tr | 1.2tr | -84.62% | -1684.04% |
|    7 | Chiến lược Ngẫu nhiên | 7.8tr | 0.8tr | -89.10% | -6.28% |
|    8 | Chiến lược Tần suất Cặp | 7.8tr | 0.8tr | -89.74% | -3372.95% |


## 📉 Biểu đồ ROI Tổng quát

> Biểu đồ thanh tương đối để nhìn nhanh chiến lược nào đang trội/yếu trong lần chạy hiện tại.
> Dấu '+' là ROI dương, dấu '-' là ROI âm. Độ dài thanh được chuẩn hóa theo giá trị tuyệt đối lớn nhất.

| Chiến lược | ROI | Biểu đồ tương đối |
|------------|-----|-------------------|
| Chiến lược Số Lạnh | 3284.84% | ++++++++++++++++++++++++ |
| Chiến lược Tần suất Cặp | 3283.21% | +++++++++++++++++++++++ |
| Chiến lược Số Nóng | 1601.06% | +++++++++++ |
| Chiến lược Suy giảm Exponential | 1599.76% | +++++++++++ |
| Chiến lược Mẫu | 1599.43% | +++++++++++ |
| Chiến lược Không Lặp lại | -80.23% | - |
| Chiến lược Ngẫu nhiên | -82.82% | - |
| Chiến lược Vắng mặt Lâu dài | -84.81% | - |


## 📋 Bảng Chiến lược Tóm tắt

> Ngày dự đoán: **2026-03-22**.
    > Bảng rút gọn: chỉ giữ các chỉ số quan trọng để dễ so sánh nhanh.

    | Chiến lược | ROI | Tóm tắt Tài chính | Giải cao nhất (kỳ gần nhất) | Phân bố Trùng khớp | 6 Hàng đầu |
    |----------|-----|-------------------|-----------------------------|--------------------|--------|
| Chiến lược Số Lạnh | 3284.84% | chi 297.2tr, lợi 10,059.8tr, roi 3284.84% | 5 số (2023-03-15, giải 5,000tr) | 5+: 2, 4: 54, 3: 655 | 15, 5, 27, 33, 4, 39 |
| Chiến lược Tần suất Cặp | 3283.21% | chi 297.2tr, lợi 10,054.9tr, roi 3283.21% | 5 số (2022-10-09, giải 5,000tr) | 5+: 2, 4: 43, 3: 668 | 42, 29, 28, 45, 31, 22 |
| Chiến lược Số Nóng | 1601.06% | chi 297.2tr, lợi 5,055.6tr, roi 1601.06% | 5 số (2023-06-09, giải 5,000tr) | 5+: 1, 4: 42, 3: 691 | 44, 26, 34, 1, 18, 43 |
| Chiến lược Suy giảm Exponential | 1599.76% | chi 297.2tr, lợi 5,051.7tr, roi 1599.76% | 5 số (2018-05-27, giải 5,000tr) | 5+: 1, 4: 37, 3: 664 | 28, 6, 31, 42, 11, 23 |
| Chiến lược Mẫu | 1599.43% | chi 297.2tr, lợi 5,050.7tr, roi 1599.43% | 5 số (2019-09-18, giải 5,000tr) | 5+: 1, 4: 30, 3: 714 | 14, 11, 2, 7, 31, 25 |
| Chiến lược Không Lặp lại | -80.23% | chi 297.2tr, lợi 58.8tr, roi -80.23% | 4 số (2025-12-26, giải 0.5tr) | 5+: 0, 4: 64, 3: 535 | 3, 5, 27, 30, 39, 41 |
| Chiến lược Ngẫu nhiên | -82.82% | chi 297.2tr, lợi 51tr, roi -82.82% | 4 số (2025-12-05, giải 0.5tr) | 5+: 0, 4: 39, 3: 631 | 32, 35, 26, 10, 6, 27 |
| Chiến lược Vắng mặt Lâu dài | -84.81% | chi 297.2tr, lợi 45.1tr, roi -84.81% | 4 số (2026-03-06, giải 0.5tr) | 5+: 0, 4: 26, 3: 643 | 39, 34, 40, 1, 27, 5 |


## 🔭 Dự đoán Số cho Lần Quay Tiếp theo

> Dự đoán cho lần quay tiếp theo vào: **2026-03-22**.
> Phương pháp: mỗi chiến lược mô phỏng **200** vé, sau đó tất cả vé được tổng hợp.
> Đây là xếp hạng xác suất, không phải các số trúng đảm bảo.

### Bảng A - 6 số ứng cử viên theo Toàn kỳ

| Số | Điểm Tập hợp | Xuất hiện trong Vé |
|--------|----------------|---------------------|
| 30 | 457 | 28.56% |
| 41 | 437 | 27.31% |
| 5 | 435 | 27.19% |
| 3 | 426 | 26.62% |
| 39 | 410 | 25.62% |
| 27 | 407 | 25.44% |

### Bảng B - 6 số ứng cử viên theo Khung nhớ động

> Trọng số chiến lược được tính theo ROI OOS trong **90 ngày gần nhất (tự động chọn)**.
> Phân bổ số bộ/chiến lược: **động theo ROI OOS (tổng 40 bộ)**.

| Số | Điểm Động (weighted) | Tỷ trọng Điểm Động |
|--------|-----------------------|--------------------|
| 30 | 6482.6 | 14.17% |
| 41 | 6462.6 | 14.12% |
| 5 | 6460.6 | 14.12% |
| 3 | 6451.6 | 14.10% |
| 39 | 6435.6 | 14.07% |
| 27 | 6432.6 | 14.06% |

### 6 hàng đầu theo Chiến lược - Bảng A (xếp theo ROI Toàn kỳ)

| Chiến lược | Giải cao nhất (kỳ gần nhất) | Số hàng đầu | x bộ số | Danh sách bộ số gợi ý |
|----------|-----------------------------|-------------|--------|------------------------|
| Chiến lược Số Lạnh | 5 số (2023-03-15, giải 5,000tr) | 41, 38, 33, 21, 19, 3 | 2 | 1. [15, 17, 19, 27, 28, 38]<br>2. [4, 6, 19, 22, 23, 30] |
| Chiến lược Tần suất Cặp | 5 số (2022-10-09, giải 5,000tr) | 45, 43, 42, 30, 29, 5 | 1 | 1. [5, 12, 19, 31, 34, 43] |
| Chiến lược Số Nóng | 5 số (2023-06-09, giải 5,000tr) | 45, 42, 35, 28, 8, 7 | 2 | 1. [3, 10, 14, 28, 44, 45]<br>2. [2, 10, 14, 17, 28, 43] |
| Chiến lược Suy giảm Exponential | 5 số (2018-05-27, giải 5,000tr) | 44, 42, 31, 28, 23, 19 | 2 | 1. [2, 8, 25, 33, 38, 44]<br>2. [7, 11, 14, 15, 23, 40] |
| Chiến lược Mẫu | 5 số (2019-09-18, giải 5,000tr) | 26, 17, 15, 9, 8, 6 | 2 | 1. [18, 20, 21, 22, 25, 31]<br>2. [3, 10, 14, 16, 20, 43] |
| Chiến lược Không Lặp lại | 4 số (2025-12-26, giải 0.5tr) | 41, 39, 30, 27, 5, 3 | 27 | 1. [3, 5, 27, 30, 39, 41]<br>2. [3, 5, 27, 30, 39, 41]<br>3. [3, 5, 27, 30, 39, 41]<br>4. [3, 5, 27, 30, 39, 41]<br>5. [3, 5, 27, 30, 39, 41]<br>6. [3, 5, 27, 30, 39, 41]<br>7. [3, 5, 27, 30, 39, 41]<br>8. [3, 5, 27, 30, 39, 41]<br>9. [3, 5, 27, 30, 39, 41]<br>10. [3, 5, 27, 30, 39, 41]<br>11. [3, 5, 27, 30, 39, 41]<br>12. [3, 5, 27, 30, 39, 41]<br>13. [3, 5, 27, 30, 39, 41]<br>14. [3, 5, 27, 30, 39, 41]<br>15. [3, 5, 27, 30, 39, 41]<br>16. [3, 5, 27, 30, 39, 41]<br>17. [3, 5, 27, 30, 39, 41]<br>18. [3, 5, 27, 30, 39, 41]<br>19. [3, 5, 27, 30, 39, 41]<br>20. [3, 5, 27, 30, 39, 41]<br>21. [3, 5, 27, 30, 39, 41]<br>22. [3, 5, 27, 30, 39, 41]<br>23. [3, 5, 27, 30, 39, 41]<br>24. [3, 5, 27, 30, 39, 41]<br>25. [3, 5, 27, 30, 39, 41]<br>26. [3, 5, 27, 30, 39, 41]<br>27. [3, 5, 27, 30, 39, 41] |
| Chiến lược Ngẫu nhiên | 4 số (2025-12-05, giải 0.5tr) | 41, 35, 30, 20, 17, 15 | 2 | 1. [15, 29, 32, 37, 40, 45]<br>2. [2, 5, 11, 18, 20, 36] |
| Chiến lược Vắng mặt Lâu dài | 4 số (2026-03-06, giải 0.5tr) | 45, 41, 39, 29, 24, 1 | 2 | 1. [1, 5, 9, 17, 27, 41]<br>2. [1, 3, 9, 34, 40, 41] |

### 6 hàng đầu theo Chiến lược - Bảng B (xếp theo ROI Khung nhớ động)

> Xếp hạng theo ROI OOS trong **90 ngày gần nhất (tự động chọn)**.

| Chiến lược | Giải cao nhất (kỳ gần nhất) | Số hàng đầu | x bộ số | Danh sách bộ số gợi ý |
|----------|-----------------------------|-------------|--------|------------------------|
| Chiến lược Không Lặp lại | 4 số (2025-12-26, giải 0.5tr) | 41, 39, 30, 27, 5, 3 | 27 | 1. [3, 5, 27, 30, 39, 41]<br>2. [3, 5, 27, 30, 39, 41]<br>3. [3, 5, 27, 30, 39, 41]<br>4. [3, 5, 27, 30, 39, 41]<br>5. [3, 5, 27, 30, 39, 41]<br>6. [3, 5, 27, 30, 39, 41]<br>7. [3, 5, 27, 30, 39, 41]<br>8. [3, 5, 27, 30, 39, 41]<br>9. [3, 5, 27, 30, 39, 41]<br>10. [3, 5, 27, 30, 39, 41]<br>11. [3, 5, 27, 30, 39, 41]<br>12. [3, 5, 27, 30, 39, 41]<br>13. [3, 5, 27, 30, 39, 41]<br>14. [3, 5, 27, 30, 39, 41]<br>15. [3, 5, 27, 30, 39, 41]<br>16. [3, 5, 27, 30, 39, 41]<br>17. [3, 5, 27, 30, 39, 41]<br>18. [3, 5, 27, 30, 39, 41]<br>19. [3, 5, 27, 30, 39, 41]<br>20. [3, 5, 27, 30, 39, 41]<br>21. [3, 5, 27, 30, 39, 41]<br>22. [3, 5, 27, 30, 39, 41]<br>23. [3, 5, 27, 30, 39, 41]<br>24. [3, 5, 27, 30, 39, 41]<br>25. [3, 5, 27, 30, 39, 41]<br>26. [3, 5, 27, 30, 39, 41]<br>27. [3, 5, 27, 30, 39, 41] |
| Chiến lược Số Lạnh | 5 số (2023-03-15, giải 5,000tr) | 41, 38, 33, 21, 19, 3 | 2 | 1. [4, 12, 19, 27, 35, 36]<br>2. [21, 22, 26, 29, 33, 45] |
| Chiến lược Số Nóng | 5 số (2023-06-09, giải 5,000tr) | 45, 42, 35, 28, 8, 7 | 2 | 1. [2, 11, 18, 23, 39, 44]<br>2. [7, 9, 19, 24, 35, 45] |
| Chiến lược Suy giảm Exponential | 5 số (2018-05-27, giải 5,000tr) | 44, 42, 31, 28, 23, 19 | 2 | 1. [4, 5, 10, 21, 26, 34]<br>2. [8, 19, 20, 27, 31, 34] |
| Chiến lược Vắng mặt Lâu dài | 4 số (2026-03-06, giải 0.5tr) | 45, 41, 39, 29, 24, 1 | 2 | 1. [1, 24, 27, 34, 40, 45]<br>2. [5, 27, 29, 34, 40, 45] |
| Chiến lược Mẫu | 5 số (2019-09-18, giải 5,000tr) | 26, 17, 15, 9, 8, 6 | 2 | 1. [1, 2, 3, 16, 36, 40]<br>2. [10, 17, 29, 32, 35, 36] |
| Chiến lược Ngẫu nhiên | 4 số (2025-12-05, giải 0.5tr) | 41, 35, 30, 20, 17, 15 | 2 | 1. [10, 20, 31, 39, 40, 43]<br>2. [4, 11, 12, 23, 27, 35] |
| Chiến lược Tần suất Cặp | 5 số (2022-10-09, giải 5,000tr) | 45, 43, 42, 30, 29, 5 | 1 | 1. [3, 8, 17, 38, 43, 45] |


## 🧪 Đánh giá Rolling Out-of-Sample

> Cửa sổ kiểm thử ngoài mẫu: **90 ngày gần nhất (tự động chọn)** (đến 2026-03-20).
> Mục tiêu: đánh giá chiến lược trên giai đoạn gần đây, giảm thiên lệch do fit vào toàn bộ lịch sử.

| Chiến lược | Giai đoạn OOS | Tài chính OOS | Phân bố trùng khớp OOS |
|------------|----------------|---------------|--------------------------|
| Chiến lược Không Lặp lại | 2025-12-21 00:00:00 → 2026-03-20 00:00:00 (780 dự đoán) | chi 7.8tr, lợi 10.2tr, roi 30.13% | 6+: 0, 5: 0, 4: 20, 3: 3 |
| Chiến lược Số Lạnh | 2025-12-21 00:00:00 → 2026-03-20 00:00:00 (780 dự đoán) | chi 7.8tr, lợi 2.8tr, roi -64.10% | 6+: 0, 5: 0, 4: 3, 3: 26 |
| Chiến lược Số Nóng | 2025-12-21 00:00:00 → 2026-03-20 00:00:00 (780 dự đoán) | chi 7.8tr, lợi 1.7tr, roi -78.21% | 6+: 0, 5: 0, 4: 1, 3: 24 |
| Chiến lược Suy giảm Exponential | 2025-12-21 00:00:00 → 2026-03-20 00:00:00 (780 dự đoán) | chi 7.8tr, lợi 1.6tr, roi -80.13% | 6+: 0, 5: 0, 4: 1, 3: 21 |
| Chiến lược Vắng mặt Lâu dài | 2025-12-21 00:00:00 → 2026-03-20 00:00:00 (780 dự đoán) | chi 7.8tr, lợi 1.3tr, roi -83.33% | 6+: 0, 5: 0, 4: 1, 3: 16 |
| Chiến lược Mẫu | 2025-12-21 00:00:00 → 2026-03-20 00:00:00 (780 dự đoán) | chi 7.8tr, lợi 1.2tr, roi -84.62% | 6+: 0, 5: 0, 4: 1, 3: 14 |
| Chiến lược Ngẫu nhiên | 2025-12-21 00:00:00 → 2026-03-20 00:00:00 (780 dự đoán) | chi 7.8tr, lợi 0.8tr, roi -89.10% | 6+: 0, 5: 0, 4: 0, 3: 17 |
| Chiến lược Tần suất Cặp | 2025-12-21 00:00:00 → 2026-03-20 00:00:00 (780 dự đoán) | chi 7.8tr, lợi 0.8tr, roi -89.74% | 6+: 0, 5: 0, 4: 0, 3: 16 |




## 🧾 Leaderboard Lịch sử

> Tổng hợp từ **18 bản ghi gần nhất** của sản phẩm `power_645`.
> Bảng này giúp ưu tiên chiến lược ổn định theo thời gian, không chỉ theo một lần chạy.

| Hạng | Chiến lược | ROI TB lịch sử | ROI Độ lệch chuẩn | Số run |
|------|------------|----------------|-------------------|--------|
| 1 | Chiến lược Ngẫu nhiên | 2569.02% | 2125.92% | 40 |
| 2 | Chiến lược Suy giảm Exponential | 1812.23% | 1514.14% | 40 |
| 3 | Chiến lược Số Lạnh | 1685.76% | 1454.58% | 40 |
| 4 | Chiến lược Mẫu | 1475.74% | 1324.41% | 40 |
| 5 | Chiến lược Vắng mặt Lâu dài | 1179.37% | 902.20% | 40 |
| 6 | Chiến lược Số Nóng | 1054.00% | 873.48% | 40 |
| 7 | Chiến lược Tần suất Cặp | 675.74% | 1125.32% | 40 |
| 8 | Chiến lược Không Lặp lại | -79.62% | 0.62% | 40 |


---

## ⚠️ Tuyên bố Miễn trách nhiệm

Tóm tắt dự đoán này chỉ dành cho mục đích giáo dục và nghiên cứu. Kết quả xổ số ngẫu nhiên và không thể dự đoán một cách đáng tin cậy. Không bao giờ cờ bạc nhiều hơn những gì bạn có thể mất được.
