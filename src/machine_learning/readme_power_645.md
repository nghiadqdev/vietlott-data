# 🔮 Tóm tắt Dự đoán Vietlott Power 645

> **Được tạo**: 2026-04-01 17:01:26
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
| 🥇 1 | Chiến lược Ngẫu nhiên | 297.2tr | 15,053.4tr | 14,756.2tr | 4965.07% |
| 🥈 2 | Chiến lược Số Lạnh | 297.2tr | 10,058tr | 9,760.9tr | 3284.27% |
| 🥉 3 | Chiến lược Suy giảm Exponential | 297.2tr | 10,054.5tr | 9,757.2tr | 3283.06% |
|    4 | Chiến lược Vắng mặt Lâu dài | 297.2tr | 10,047.2tr | 9,750tr | 3280.64% |
|    5 | Chiến lược Mẫu | 297.2tr | 5,056.6tr | 4,759.4tr | 1601.41% |
|    6 | Chiến lược Số Nóng | 297.2tr | 5,049.6tr | 4,752.4tr | 1599.04% |
|    7 | Chiến lược Không Lặp lại | 297.2tr | 63.7tr | -233.5tr | -78.57% |
|    8 | Chiến lược Tần suất Cặp | 297.2tr | 57.2tr | -240tr | -80.75% |


## 📊 So sánh ROI: Benchmark vs Khung nhớ động

> Bảng A là benchmark cố định trên toàn bộ lịch sử.
> Bảng B là ROI ở cửa sổ gần đây **180 ngày gần nhất (tự động chọn)** để mô phỏng vận hành động.
> Cột **ΔROI** giúp bạn thấy mức thay đổi khi chuyển từ khung nhớ cố định sang khung nhớ gần.

### Bảng A: ROI Benchmark (Toàn kỳ)

| Hạng | Chiến lược | Tổng Chi phí (tr) | Tổng Lợi nhuận (tr) | Lợi nhuận ròng (tr) | ROI Toàn kỳ |
|------|------------|-------------------|---------------------|---------------------|-------------|
| 🥇 1 | Chiến lược Ngẫu nhiên | 297.2tr | 15,053.4tr | 14,756.2tr | 4965.07% |
| 🥈 2 | Chiến lược Số Lạnh | 297.2tr | 10,058tr | 9,760.9tr | 3284.27% |
| 🥉 3 | Chiến lược Suy giảm Exponential | 297.2tr | 10,054.5tr | 9,757.2tr | 3283.06% |
|    4 | Chiến lược Vắng mặt Lâu dài | 297.2tr | 10,047.2tr | 9,750tr | 3280.64% |
|    5 | Chiến lược Mẫu | 297.2tr | 5,056.6tr | 4,759.4tr | 1601.41% |
|    6 | Chiến lược Số Nóng | 297.2tr | 5,049.6tr | 4,752.4tr | 1599.04% |
|    7 | Chiến lược Không Lặp lại | 297.2tr | 63.7tr | -233.5tr | -78.57% |
|    8 | Chiến lược Tần suất Cặp | 297.2tr | 57.2tr | -240tr | -80.75% |

### Bảng B: ROI Khung nhớ động (OOS gần đây)

| Hạng | Chiến lược | Chi phí OOS (tr) | Lợi nhuận OOS (tr) | ROI OOS | ΔROI (OOS - Toàn kỳ) |
|------|------------|------------------|--------------------|---------|-----------------------|
| 🥇 1 | Chiến lược Suy giảm Exponential | 15.6tr | 5,003.1tr | 31971.15% | +28688.10% |
| 🥈 2 | Chiến lược Không Lặp lại | 15.6tr | 11.2tr | -28.53% | +50.04% |
| 🥉 3 | Chiến lược Số Lạnh | 15.6tr | 3tr | -80.45% | -3364.72% |
|    4 | Chiến lược Số Nóng | 15.6tr | 2.6tr | -83.01% | -1682.05% |
|    5 | Chiến lược Vắng mặt Lâu dài | 15.6tr | 2.4tr | -84.62% | -3365.25% |
|    6 | Chiến lược Tần suất Cặp | 15.6tr | 2.2tr | -85.58% | -4.82% |
|    7 | Chiến lược Ngẫu nhiên | 15.6tr | 2tr | -86.86% | -5051.93% |
|    8 | Chiến lược Mẫu | 15.6tr | 2tr | -86.86% | -1688.27% |


## 📉 Biểu đồ ROI Tổng quát

> Biểu đồ thanh tương đối để nhìn nhanh chiến lược nào đang trội/yếu trong lần chạy hiện tại.
> Dấu '+' là ROI dương, dấu '-' là ROI âm. Độ dài thanh được chuẩn hóa theo giá trị tuyệt đối lớn nhất.

| Chiến lược | ROI | Biểu đồ tương đối |
|------------|-----|-------------------|
| Chiến lược Ngẫu nhiên | 4965.07% | ++++++++++++++++++++++++ |
| Chiến lược Số Lạnh | 3284.27% | +++++++++++++++ |
| Chiến lược Suy giảm Exponential | 3283.06% | +++++++++++++++ |
| Chiến lược Vắng mặt Lâu dài | 3280.64% | +++++++++++++++ |
| Chiến lược Mẫu | 1601.41% | +++++++ |
| Chiến lược Số Nóng | 1599.04% | +++++++ |
| Chiến lược Không Lặp lại | -78.57% | - |
| Chiến lược Tần suất Cặp | -80.75% | - |


## 📋 Bảng Chiến lược Tóm tắt

> Ngày dự đoán: **2026-03-22**.
> Dạng tóm tắt: Cấu hình, Kỳ Kiểm thử, Tóm tắt Tài chính, Phân bố Trùng khớp, KQ nổi bật (>=5 số trùng), 6 Hàng đầu.

| Chiến lược | Cấu hình | Kỳ Kiểm thử | Tóm tắt Tài chính | Phân bố Trùng khớp | KQ nổi bật (>=5) | 6 Hàng đầu |
|----------|---------------|-----------------|-------------------|--------------------|--------------|--------|
| Chiến lược Ngẫu nhiên | dải 1-45, chọn 6, vé/ngày 20 | 2016-07-20 00:00:00 → 2026-03-20 00:00:00 (1,486 lần quay/29,720 dự đoán) | chi 297.2tr, lợi 15,053.4tr, roi 4965.07% | 5+: 3, 4: 45, 3: 618 | 3 hàng với >=5 số trùng | 19, 25, 44, 30, 16, 40 |
| Chiến lược Số Lạnh | dải 1-45, chọn 6, vé/ngày 20 | 2016-07-20 00:00:00 → 2026-03-20 00:00:00 (1,486 lần quay/29,720 dự đoán) | chi 297.2tr, lợi 10,058tr, roi 3284.27% | 5+: 2, 4: 51, 3: 651 | 2 hàng với >=5 số trùng | 3, 39, 27, 25, 11, 12 |
| Chiến lược Suy giảm Exponential | dải 1-45, chọn 6, vé/ngày 20 | 2016-07-20 00:00:00 → 2026-03-20 00:00:00 (1,486 lần quay/29,720 dự đoán) | chi 297.2tr, lợi 10,054.5tr, roi 3283.06% | 5+: 2, 4: 45, 3: 639 | 2 hàng với >=5 số trùng | 42, 28, 23, 20, 31, 43 |
| Chiến lược Vắng mặt Lâu dài | dải 1-45, chọn 6, vé/ngày 20 | 2016-07-20 00:00:00 → 2026-03-20 00:00:00 (1,486 lần quay/29,720 dự đoán) | chi 297.2tr, lợi 10,047.2tr, roi 3280.64% | 5+: 2, 4: 33, 3: 615 | 2 hàng với >=5 số trùng | 27, 40, 9, 45, 17, 1 |
| Chiến lược Mẫu | dải 1-45, chọn 6, vé/ngày 20 | 2016-07-20 00:00:00 → 2026-03-20 00:00:00 (1,486 lần quay/29,720 dự đoán) | chi 297.2tr, lợi 5,056.6tr, roi 1601.41% | 5+: 1, 4: 46, 3: 672 | 1 hàng với >=5 số trùng | 9, 7, 3, 6, 2, 8 |
| Chiến lược Số Nóng | dải 1-45, chọn 6, vé/ngày 20 | 2016-07-20 00:00:00 → 2026-03-20 00:00:00 (1,486 lần quay/29,720 dự đoán) | chi 297.2tr, lợi 5,049.6tr, roi 1599.04% | 5+: 1, 4: 35, 3: 641 | 1 hàng với >=5 số trùng | 28, 45, 43, 8, 40, 30 |
| Chiến lược Không Lặp lại | dải 1-45, chọn 6, vé/ngày 20 | 2016-07-20 00:00:00 → 2026-03-20 00:00:00 (1,486 lần quay/29,720 dự đoán) | chi 297.2tr, lợi 63.7tr, roi -78.57% | 5+: 0, 4: 75, 3: 524 | 0 hàng với >=5 số trùng | 3, 5, 27, 30, 39, 41 |
| Chiến lược Tần suất Cặp | dải 1-45, chọn 6, vé/ngày 20 | 2016-07-20 00:00:00 → 2026-03-20 00:00:00 (1,486 lần quay/29,720 dự đoán) | chi 297.2tr, lợi 57.2tr, roi -80.75% | 5+: 0, 4: 48, 3: 664 | 0 hàng với >=5 số trùng | 42, 45, 8, 13, 43, 5 |


## 🔭 Dự đoán Số cho Lần Quay Tiếp theo

> Dự đoán cho lần quay tiếp theo vào: **2026-03-22**.
> Phương pháp: mỗi chiến lược mô phỏng **200** vé, sau đó tất cả vé được tổng hợp.
> Đây là xếp hạng xác suất, không phải các số trúng đảm bảo.

### Bảng A - 6 số ứng cử viên theo Toàn kỳ

| Số | Điểm Tập hợp | Xuất hiện trong Vé |
|--------|----------------|---------------------|
| 39 | 452 | 28.25% |
| 3 | 446 | 27.88% |
| 5 | 431 | 26.94% |
| 27 | 423 | 26.44% |
| 41 | 422 | 26.38% |
| 30 | 420 | 26.25% |

### Bảng B - 6 số ứng cử viên theo Khung nhớ động

> Trọng số chiến lược được tính theo ROI OOS trong **180 ngày gần nhất (tự động chọn)**.
> Phân bổ số bộ/chiến lược: **động theo ROI OOS (tổng 40 bộ)**.

| Số | Điểm Động (weighted) | Tỷ trọng Điểm Động |
|--------|-----------------------|--------------------|
| 45 | 1215139.8 | 3.17% |
| 20 | 1215057.8 | 3.17% |
| 9 | 1183193.7 | 3.08% |
| 2 | 1183110.7 | 3.08% |
| 42 | 1151130.5 | 3.00% |
| 28 | 1087205.2 | 2.83% |

### 6 hàng đầu theo Chiến lược - Bảng A (xếp theo ROI Toàn kỳ)

| Chiến lược | Số hàng đầu | x bộ số | Danh sách bộ số gợi ý |
|----------|-------------|--------|------------------------|
| Chiến lược Ngẫu nhiên | 42, 39, 32, 26, 19, 5 | 1 | 1. [7, 24, 25, 27, 34, 35] |
| Chiến lược Số Lạnh | 40, 34, 33, 25, 19, 11 | 1 | 1. [3, 5, 16, 25, 39, 41] |
| Chiến lược Suy giảm Exponential | 45, 42, 28, 20, 9, 2 | 33 | 1. [4, 11, 17, 22, 26, 27]<br>2. [4, 10, 39, 42, 43, 45]<br>3. [7, 10, 23, 25, 31, 44]<br>4. [6, 19, 29, 30, 33, 39]<br>5. [2, 11, 23, 24, 39, 41]<br>6. [8, 20, 27, 28, 36, 44]<br>7. [1, 9, 20, 29, 34, 40]<br>8. [21, 28, 31, 32, 34, 40]<br>9. [20, 22, 32, 33, 41, 45]<br>10. [8, 12, 17, 18, 29, 34]<br>11. [5, 12, 33, 35, 43, 44]<br>12. [8, 16, 20, 24, 25, 42]<br>13. [4, 15, 20, 36, 43, 45]<br>14. [3, 4, 16, 21, 24, 43]<br>15. [16, 20, 24, 29, 36, 41]<br>16. [4, 11, 16, 19, 20, 32]<br>17. [12, 29, 38, 42, 44, 45]<br>18. [12, 18, 23, 26, 29, 34]<br>19. [13, 15, 17, 18, 22, 43]<br>20. [13, 16, 24, 32, 34, 36]<br>21. [1, 6, 8, 17, 30, 34]<br>22. [1, 8, 11, 12, 30, 40]<br>23. [4, 15, 18, 26, 33, 39]<br>24. [6, 14, 15, 31, 34, 35]<br>25. [1, 11, 12, 15, 20, 31]<br>26. [17, 19, 20, 22, 38, 45]<br>27. [10, 13, 18, 25, 29, 34]<br>28. [2, 13, 17, 23, 36, 42]<br>29. [16, 18, 22, 34, 35, 37]<br>30. [2, 11, 14, 34, 37, 43]<br>31. [7, 15, 20, 28, 39, 43]<br>32. [7, 8, 16, 26, 28, 37]<br>33. [13, 15, 23, 28, 32, 36] |
| Chiến lược Vắng mặt Lâu dài | 40, 34, 29, 9, 3, 1 | 1 | 1. [1, 5, 24, 27, 29, 30] |
| Chiến lược Mẫu | 37, 34, 31, 8, 3, 2 | 1 | 1. [4, 11, 20, 37, 38, 39] |
| Chiến lược Số Nóng | 45, 44, 43, 42, 37, 13 | 1 | 1. [5, 11, 16, 24, 30, 39] |
| Chiến lược Không Lặp lại | 41, 39, 30, 27, 5, 3 | 1 | 1. [3, 5, 27, 30, 39, 41] |
| Chiến lược Tần suất Cặp | 45, 29, 28, 23, 9, 7 | 1 | 1. [9, 10, 16, 21, 22, 32] |

### 6 hàng đầu theo Chiến lược - Bảng B (xếp theo ROI Khung nhớ động)

> Xếp hạng theo ROI OOS trong **180 ngày gần nhất (tự động chọn)**.

| Chiến lược | Số hàng đầu | x bộ số | Danh sách bộ số gợi ý |
|----------|-------------|--------|------------------------|
| Chiến lược Suy giảm Exponential | 45, 42, 28, 20, 9, 2 | 33 | 1. [3, 7, 10, 14, 21, 32]<br>2. [9, 10, 12, 24, 35, 42]<br>3. [3, 6, 16, 26, 40, 45]<br>4. [1, 3, 11, 13, 20, 44]<br>5. [14, 20, 28, 30, 35, 37]<br>6. [1, 8, 11, 16, 23, 30]<br>7. [20, 28, 31, 34, 39, 41]<br>8. [1, 15, 20, 40, 44, 45]<br>9. [7, 28, 34, 38, 44, 45]<br>10. [4, 6, 23, 34, 38, 45]<br>11. [2, 11, 23, 28, 30, 35]<br>12. [3, 16, 18, 22, 27, 39]<br>13. [2, 10, 15, 20, 24, 38]<br>14. [9, 11, 26, 29, 39, 43]<br>15. [2, 26, 31, 37, 38, 42]<br>16. [3, 16, 18, 36, 38, 39]<br>17. [6, 9, 19, 31, 32, 43]<br>18. [1, 11, 18, 27, 35, 36]<br>19. [1, 7, 18, 20, 24, 29]<br>20. [4, 11, 20, 38, 39, 42]<br>21. [4, 9, 13, 30, 38, 45]<br>22. [6, 9, 15, 16, 29, 40]<br>23. [1, 5, 9, 20, 31, 37]<br>24. [25, 29, 31, 32, 37, 43]<br>25. [2, 19, 22, 28, 34, 40]<br>26. [2, 7, 20, 23, 24, 39]<br>27. [5, 9, 10, 15, 25, 35]<br>28. [15, 16, 20, 23, 27, 36]<br>29. [1, 3, 16, 20, 36, 41]<br>30. [2, 6, 8, 16, 18, 37]<br>31. [4, 21, 26, 27, 28, 31]<br>32. [17, 18, 20, 34, 36, 42]<br>33. [13, 15, 16, 17, 20, 42] |
| Chiến lược Không Lặp lại | 41, 39, 30, 27, 5, 3 | 1 | 1. [3, 5, 27, 30, 39, 41] |
| Chiến lược Số Lạnh | 40, 34, 33, 25, 19, 11 | 1 | 1. [9, 12, 20, 32, 33, 45] |
| Chiến lược Số Nóng | 45, 44, 43, 42, 37, 13 | 1 | 1. [1, 2, 4, 7, 17, 31] |
| Chiến lược Vắng mặt Lâu dài | 40, 34, 29, 9, 3, 1 | 1 | 1. [1, 29, 30, 34, 40, 45] |
| Chiến lược Tần suất Cặp | 45, 29, 28, 23, 9, 7 | 1 | 1. [2, 10, 20, 27, 28, 31] |
| Chiến lược Ngẫu nhiên | 42, 39, 32, 26, 19, 5 | 1 | 1. [4, 7, 16, 26, 29, 43] |
| Chiến lược Mẫu | 37, 34, 31, 8, 3, 2 | 1 | 1. [6, 7, 8, 9, 10, 32] |


## 🧪 Đánh giá Rolling Out-of-Sample

> Cửa sổ kiểm thử ngoài mẫu: **180 ngày gần nhất (tự động chọn)** (đến 2026-03-20).
> Mục tiêu: đánh giá chiến lược trên giai đoạn gần đây, giảm thiên lệch do fit vào toàn bộ lịch sử.

| Chiến lược | Giai đoạn OOS | Tài chính OOS | Phân bố trùng khớp OOS |
|------------|----------------|---------------|--------------------------|
| Chiến lược Suy giảm Exponential | 2025-09-21 00:00:00 → 2026-03-20 00:00:00 (1,560 dự đoán) | chi 15.6tr, lợi 5,003.1tr, roi 31971.15% | 6+: 0, 5: 1, 4: 3, 3: 32 |
| Chiến lược Không Lặp lại | 2025-09-21 00:00:00 → 2026-03-20 00:00:00 (1,560 dự đoán) | chi 15.6tr, lợi 11.2tr, roi -28.53% | 6+: 0, 5: 0, 4: 20, 3: 23 |
| Chiến lược Số Lạnh | 2025-09-21 00:00:00 → 2026-03-20 00:00:00 (1,560 dự đoán) | chi 15.6tr, lợi 3tr, roi -80.45% | 6+: 0, 5: 0, 4: 2, 3: 41 |
| Chiến lược Số Nóng | 2025-09-21 00:00:00 → 2026-03-20 00:00:00 (1,560 dự đoán) | chi 15.6tr, lợi 2.6tr, roi -83.01% | 6+: 0, 5: 0, 4: 2, 3: 33 |
| Chiến lược Vắng mặt Lâu dài | 2025-09-21 00:00:00 → 2026-03-20 00:00:00 (1,560 dự đoán) | chi 15.6tr, lợi 2.4tr, roi -84.62% | 6+: 0, 5: 0, 4: 2, 3: 28 |
| Chiến lược Tần suất Cặp | 2025-09-21 00:00:00 → 2026-03-20 00:00:00 (1,560 dự đoán) | chi 15.6tr, lợi 2.2tr, roi -85.58% | 6+: 0, 5: 0, 4: 2, 3: 25 |
| Chiến lược Ngẫu nhiên | 2025-09-21 00:00:00 → 2026-03-20 00:00:00 (1,560 dự đoán) | chi 15.6tr, lợi 2tr, roi -86.86% | 6+: 0, 5: 0, 4: 1, 3: 31 |
| Chiến lược Mẫu | 2025-09-21 00:00:00 → 2026-03-20 00:00:00 (1,560 dự đoán) | chi 15.6tr, lợi 2tr, roi -86.86% | 6+: 0, 5: 0, 4: 1, 3: 31 |




## 🧾 Leaderboard Lịch sử

> Tổng hợp từ **17 bản ghi gần nhất** của sản phẩm `power_645`.
> Bảng này giúp ưu tiên chiến lược ổn định theo thời gian, không chỉ theo một lần chạy.

| Hạng | Chiến lược | ROI TB lịch sử | ROI Độ lệch chuẩn | Số run |
|------|------------|----------------|-------------------|--------|
| 1 | Chiến lược Ngẫu nhiên | 2507.58% | 2117.65% | 39 |
| 2 | Chiến lược Suy giảm Exponential | 1774.52% | 1514.76% | 39 |
| 3 | Chiến lược Số Lạnh | 1644.78% | 1450.12% | 39 |
| 4 | Chiến lược Mẫu | 1472.52% | 1341.13% | 39 |
| 5 | Chiến lược Vắng mặt Lâu dài | 1125.49% | 847.77% | 39 |
| 6 | Chiến lược Số Nóng | 1040.03% | 880.19% | 39 |
| 7 | Chiến lược Tần suất Cặp | 695.14% | 1133.03% | 39 |
| 8 | Chiến lược Không Lặp lại | -79.65% | 0.61% | 39 |


---

## ⚠️ Tuyên bố Miễn trách nhiệm

Tóm tắt dự đoán này chỉ dành cho mục đích giáo dục và nghiên cứu. Kết quả xổ số ngẫu nhiên và không thể dự đoán một cách đáng tin cậy. Không bao giờ cờ bạc nhiều hơn những gì bạn có thể mất được.
