# 🔮 Tóm tắt Dự đoán Vietlott Power 645

> **Được tạo**: 2026-04-05 13:00:49
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
| 🥇 1 | Chiến lược Tần suất Cặp | 297.2tr | 15,052tr | 14,754.8tr | 4964.60% |
| 🥈 2 | Chiến lược Ngẫu nhiên | 297.2tr | 10,052.6tr | 9,755.5tr | 3282.45% |
| 🥉 3 | Chiến lược Số Lạnh | 297.2tr | 5,052.7tr | 4,755.5tr | 1600.10% |
|    4 | Chiến lược Suy giảm Exponential | 297.2tr | 5,052.6tr | 4,755.4tr | 1600.08% |
|    5 | Chiến lược Không Lặp lại | 297.2tr | 59.4tr | -237.8tr | -80.03% |
|    6 | Chiến lược Mẫu | 297.2tr | 52.5tr | -244.7tr | -82.32% |
|    7 | Chiến lược Số Nóng | 297.2tr | 50.4tr | -246.8tr | -83.04% |
|    8 | Chiến lược Vắng mặt Lâu dài | 297.2tr | 45.4tr | -251.8tr | -84.72% |


## 📊 So sánh ROI: Benchmark vs Khung nhớ động

> Bảng A là benchmark cố định trên toàn bộ lịch sử.
> Bảng B là ROI ở cửa sổ gần đây **60 ngày gần nhất (tự động chọn)** để mô phỏng vận hành động.
> Cột **ΔROI** giúp bạn thấy mức thay đổi khi chuyển từ khung nhớ cố định sang khung nhớ gần.

### Bảng A: ROI Benchmark (Toàn kỳ)

| Hạng | Chiến lược | Tổng Chi phí (tr) | Tổng Lợi nhuận (tr) | Lợi nhuận ròng (tr) | ROI Toàn kỳ |
|------|------------|-------------------|---------------------|---------------------|-------------|
| 🥇 1 | Chiến lược Tần suất Cặp | 297.2tr | 15,052tr | 14,754.8tr | 4964.60% |
| 🥈 2 | Chiến lược Ngẫu nhiên | 297.2tr | 10,052.6tr | 9,755.5tr | 3282.45% |
| 🥉 3 | Chiến lược Số Lạnh | 297.2tr | 5,052.7tr | 4,755.5tr | 1600.10% |
|    4 | Chiến lược Suy giảm Exponential | 297.2tr | 5,052.6tr | 4,755.4tr | 1600.08% |
|    5 | Chiến lược Không Lặp lại | 297.2tr | 59.4tr | -237.8tr | -80.03% |
|    6 | Chiến lược Mẫu | 297.2tr | 52.5tr | -244.7tr | -82.32% |
|    7 | Chiến lược Số Nóng | 297.2tr | 50.4tr | -246.8tr | -83.04% |
|    8 | Chiến lược Vắng mặt Lâu dài | 297.2tr | 45.4tr | -251.8tr | -84.72% |

### Bảng B: ROI Khung nhớ động (OOS gần đây)

| Hạng | Chiến lược | Chi phí OOS (tr) | Lợi nhuận OOS (tr) | ROI OOS | ΔROI (OOS - Toàn kỳ) |
|------|------------|------------------|--------------------|---------|-----------------------|
| 🥇 1 | Chiến lược Ngẫu nhiên | 5.2tr | 5,001.6tr | 96085.58% | +92803.12% |
| 🥈 2 | Chiến lược Suy giảm Exponential | 5.2tr | 1.8tr | -66.35% | -1666.43% |
| 🥉 3 | Chiến lược Không Lặp lại | 5.2tr | 1.2tr | -76.92% | +3.11% |
|    4 | Chiến lược Mẫu | 5.2tr | 1.1tr | -79.81% | +2.51% |
|    5 | Chiến lược Số Nóng | 5.2tr | 1tr | -80.77% | +2.27% |
|    6 | Chiến lược Vắng mặt Lâu dài | 5.2tr | 0.8tr | -85.58% | -0.85% |
|    7 | Chiến lược Số Lạnh | 5.2tr | 0.7tr | -87.50% | -1687.60% |
|    8 | Chiến lược Tần suất Cặp | 5.2tr | 0.5tr | -90.38% | -5054.99% |


## 📉 Biểu đồ ROI Tổng quát

> Biểu đồ thanh tương đối để nhìn nhanh chiến lược nào đang trội/yếu trong lần chạy hiện tại.
> Dấu '+' là ROI dương, dấu '-' là ROI âm. Độ dài thanh được chuẩn hóa theo giá trị tuyệt đối lớn nhất.

| Chiến lược | ROI | Biểu đồ tương đối |
|------------|-----|-------------------|
| Chiến lược Tần suất Cặp | 4964.60% | ++++++++++++++++++++++++ |
| Chiến lược Ngẫu nhiên | 3282.45% | +++++++++++++++ |
| Chiến lược Số Lạnh | 1600.10% | +++++++ |
| Chiến lược Suy giảm Exponential | 1600.08% | +++++++ |
| Chiến lược Không Lặp lại | -80.03% | - |
| Chiến lược Mẫu | -82.32% | - |
| Chiến lược Số Nóng | -83.04% | - |
| Chiến lược Vắng mặt Lâu dài | -84.72% | - |


## 📋 Bảng Chiến lược Tóm tắt

> Ngày dự đoán: **2026-03-22**.
> Bảng rút gọn: chỉ giữ các chỉ số quan trọng để dễ so sánh nhanh.

| Chiến lược | ROI | Tóm tắt Tài chính | Giải cao nhất (kỳ gần nhất) | Phân bố Trùng khớp | 6 Hàng đầu |
|----------|-----|-------------------|-----------------------------|--------------------|--------|
| Chiến lược Tần suất Cặp | 4964.60% | chi 297.2tr, lợi 15,052tr, roi 4964.60% | 5 số (2025-05-07, giải 5,000tr) | 5+: 3, 4: 33, 3: 710 | 7, 31, 45, 44, 43, 13 |
| Chiến lược Ngẫu nhiên | 3282.45% | chi 297.2tr, lợi 10,052.6tr, roi 3282.45% | 5 số (2026-02-13, giải 5,000tr) | 5+: 2, 4: 38, 3: 673 | 42, 30, 13, 19, 35, 4 |
| Chiến lược Số Lạnh | 1600.10% | chi 297.2tr, lợi 5,052.7tr, roi 1600.10% | 5 số (2022-10-19, giải 5,000tr) | 5+: 1, 4: 42, 3: 634 | 15, 12, 30, 39, 5, 27 |
| Chiến lược Suy giảm Exponential | 1600.08% | chi 297.2tr, lợi 5,052.6tr, roi 1600.08% | 5 số (2022-07-08, giải 5,000tr) | 5+: 1, 4: 44, 3: 613 | 31, 23, 30, 42, 28, 8 |
| Chiến lược Không Lặp lại | -80.03% | chi 297.2tr, lợi 59.4tr, roi -80.03% | 4 số (2026-03-06, giải 0.5tr) | 5+: 0, 4: 66, 3: 527 | 3, 5, 27, 30, 39, 41 |
| Chiến lược Mẫu | -82.32% | chi 297.2tr, lợi 52.5tr, roi -82.32% | 4 số (2026-02-27, giải 0.5tr) | 5+: 0, 4: 39, 3: 661 | 5, 20, 6, 8, 4, 33 |
| Chiến lược Số Nóng | -83.04% | chi 297.2tr, lợi 50.4tr, roi -83.04% | 4 số (2026-02-06, giải 0.5tr) | 5+: 0, 4: 29, 3: 718 | 45, 29, 2, 15, 11, 28 |
| Chiến lược Vắng mặt Lâu dài | -84.72% | chi 297.2tr, lợi 45.4tr, roi -84.72% | 4 số (2026-03-06, giải 0.5tr) | 5+: 0, 4: 29, 3: 618 | 30, 40, 1, 15, 39, 24 |


## 🎯 So sánh Trùng khớp Với Kỳ trước

> Bảng này chỉ hiển thị lại kết quả đã chạy trước đó (kỳ gần nhất trong tập evaluate của từng chiến lược).
> Các số trùng giữa bộ số chiến lược và kết quả trúng kỳ trước được tô **đỏ** để dễ nhìn.

| Chiến lược | Kỳ trước | Bộ số chiến lược (số trùng màu đỏ) | Kết quả trúng kỳ trước (số trùng màu đỏ) | Số trùng |
|------------|----------|-------------------------------------|-------------------------------------------|----------|
| Chiến lược Mẫu | 2026-03-20 00:00:00 | 1, 5, <span style='color:#d00000;font-weight:700'>11</span>, 14, 17, <span style='color:#d00000;font-weight:700'>43</span> | 8, <span style='color:#d00000;font-weight:700'>11</span>, 22, 23, 38, <span style='color:#d00000;font-weight:700'>43</span> | 2 |
| Chiến lược Số Nóng | 2026-03-20 00:00:00 | 2, <span style='color:#d00000;font-weight:700'>11</span>, 21, 25, 32, <span style='color:#d00000;font-weight:700'>43</span> | 8, <span style='color:#d00000;font-weight:700'>11</span>, 22, 23, 38, <span style='color:#d00000;font-weight:700'>43</span> | 2 |
| Chiến lược Ngẫu nhiên | 2026-03-20 00:00:00 | 7, <span style='color:#d00000;font-weight:700'>22</span>, 24, 30, 31, 45 | 8, 11, <span style='color:#d00000;font-weight:700'>22</span>, 23, 38, 43 | 1 |
| Chiến lược Vắng mặt Lâu dài | 2026-03-20 00:00:00 | 3, <span style='color:#d00000;font-weight:700'>8</span>, 15, 24, 27, 34 | <span style='color:#d00000;font-weight:700'>8</span>, 11, 22, 23, 38, 43 | 1 |
| Chiến lược Số Lạnh | 2026-03-20 00:00:00 | 12, 21, 24, 31, <span style='color:#d00000;font-weight:700'>38</span>, 45 | 8, 11, 22, 23, <span style='color:#d00000;font-weight:700'>38</span>, 43 | 1 |
| Chiến lược Không Lặp lại | 2026-03-20 00:00:00 | 3, 27, 30, 39, 41, <span style='color:#d00000;font-weight:700'>43</span> | 8, 11, 22, 23, 38, <span style='color:#d00000;font-weight:700'>43</span> | 1 |
| Chiến lược Suy giảm Exponential | 2026-03-20 00:00:00 | 3, 10, 26, 35, <span style='color:#d00000;font-weight:700'>38</span>, 40 | 8, 11, 22, 23, <span style='color:#d00000;font-weight:700'>38</span>, 43 | 1 |
| Chiến lược Tần suất Cặp | 2026-03-20 00:00:00 | 1, 5, 7, 37, 41, 44 | 8, 11, 22, 23, 38, 43 | 0 |


## 🔭 Dự đoán Số cho Lần Quay Tiếp theo

> Dự đoán cho lần quay tiếp theo vào: **2026-03-22**.
> Phương pháp: mỗi chiến lược mô phỏng **200** vé, sau đó tất cả vé được tổng hợp.
> Đây là xếp hạng xác suất, không phải các số trúng đảm bảo.

### Bảng A - 6 số ứng cử viên theo Toàn kỳ

| Số | Điểm Tập hợp | Xuất hiện trong Vé |
|--------|----------------|---------------------|
| 5 | 467 | 29.19% |
| 30 | 443 | 27.69% |
| 41 | 435 | 27.19% |
| 39 | 430 | 26.88% |
| 3 | 428 | 26.75% |
| 27 | 414 | 25.87% |

### Bảng B - 6 số ứng cử viên theo Khung nhớ động

> Trọng số chiến lược được tính theo ROI OOS trong **60 ngày gần nhất (tự động chọn)**.
> Phân bổ số bộ/chiến lược: **động theo ROI OOS (tổng 40 bộ)**.

| Số | Điểm Động (weighted) | Tỷ trọng Điểm Động |
|--------|-----------------------|--------------------|
| 17 | 3747602.5 | 3.25% |
| 40 | 3363227.2 | 2.92% |
| 25 | 3363153.2 | 2.92% |
| 30 | 3267352.6 | 2.83% |
| 10 | 3267087.6 | 2.83% |
| 23 | 3267072.6 | 2.83% |

### 6 hàng đầu theo Chiến lược - Bảng A (xếp theo ROI Toàn kỳ)

| Chiến lược | Giải cao nhất (kỳ gần nhất) | Số hàng đầu | x bộ số | Danh sách bộ số gợi ý |
|----------|-----------------------------|-------------|--------|------------------------|
| Chiến lược Tần suất Cặp | 5 số (2025-05-07, giải 5,000tr) | 45, 43, 42, 28, 7, 2 | 1 | 1. [17, 22, 24, 33, 38, 39] |
| Chiến lược Ngẫu nhiên | 5 số (2026-02-13, giải 5,000tr) | 40, 30, 25, 23, 17, 10 | 33 | 1. [8, 11, 20, 27, 30, 38]<br>2. [6, 20, 22, 25, 35, 40]<br>3. [1, 4, 8, 9, 31, 43]<br>4. [1, 19, 20, 27, 35, 40]<br>5. [4, 7, 10, 18, 30, 45]<br>6. [9, 17, 27, 30, 31, 37]<br>7. [14, 18, 26, 36, 38, 43]<br>8. [3, 14, 19, 26, 30, 43]<br>9. [3, 5, 12, 14, 19, 28]<br>10. [2, 13, 20, 22, 25, 26]<br>11. [15, 30, 32, 34, 36, 43]<br>12. [5, 7, 10, 22, 23, 25]<br>13. [17, 20, 22, 29, 30, 44]<br>14. [10, 12, 14, 33, 38, 44]<br>15. [11, 24, 31, 35, 39, 43]<br>16. [12, 18, 25, 26, 43, 45]<br>17. [3, 5, 7, 18, 30, 31]<br>18. [11, 16, 23, 24, 27, 35]<br>19. [6, 9, 19, 32, 35, 36]<br>20. [3, 18, 21, 25, 37, 38]<br>21. [1, 16, 18, 24, 41, 45]<br>22. [9, 29, 34, 39, 40, 44]<br>23. [6, 8, 14, 19, 22, 43]<br>24. [5, 7, 14, 24, 31, 43]<br>25. [2, 9, 17, 28, 42, 44]<br>26. [6, 11, 14, 15, 25, 42]<br>27. [13, 17, 25, 34, 43, 44]<br>28. [21, 28, 34, 40, 41, 43]<br>29. [1, 8, 26, 28, 37, 44]<br>30. [1, 15, 22, 23, 24, 40]<br>31. [9, 15, 18, 26, 30, 41]<br>32. [9, 10, 25, 26, 35, 44]<br>33. [26, 27, 31, 32, 41, 43] |
| Chiến lược Số Lạnh | 5 số (2022-10-19, giải 5,000tr) | 41, 40, 33, 9, 5, 3 | 1 | 1. [3, 4, 9, 16, 24, 33] |
| Chiến lược Suy giảm Exponential | 5 số (2022-07-08, giải 5,000tr) | 45, 44, 43, 23, 22, 17 | 1 | 1. [4, 6, 18, 24, 28, 30] |
| Chiến lược Không Lặp lại | 4 số (2026-03-06, giải 0.5tr) | 41, 39, 30, 27, 5, 3 | 1 | 1. [3, 5, 27, 30, 39, 41] |
| Chiến lược Mẫu | 4 số (2026-02-27, giải 0.5tr) | 35, 29, 16, 8, 5, 2 | 1 | 1. [4, 6, 7, 20, 26, 44] |
| Chiến lược Số Nóng | 4 số (2026-02-06, giải 0.5tr) | 42, 28, 14, 13, 10, 7 | 1 | 1. [12, 15, 28, 29, 34, 44] |
| Chiến lược Vắng mặt Lâu dài | 4 số (2026-03-06, giải 0.5tr) | 41, 39, 17, 9, 3, 1 | 1 | 1. [3, 15, 27, 29, 30, 39] |

### 6 hàng đầu theo Chiến lược - Bảng B (xếp theo ROI Khung nhớ động)

> Xếp hạng theo ROI OOS trong **60 ngày gần nhất (tự động chọn)**.

| Chiến lược | Giải cao nhất (kỳ gần nhất) | Số hàng đầu | x bộ số | Danh sách bộ số gợi ý |
|----------|-----------------------------|-------------|--------|------------------------|
| Chiến lược Ngẫu nhiên | 5 số (2026-02-13, giải 5,000tr) | 40, 30, 25, 23, 17, 10 | 33 | 1. [14, 18, 21, 29, 33, 43]<br>2. [2, 4, 12, 28, 35, 45]<br>3. [8, 25, 27, 32, 41, 44]<br>4. [4, 15, 18, 19, 32, 37]<br>5. [2, 7, 9, 12, 20, 44]<br>6. [14, 19, 31, 35, 36, 44]<br>7. [19, 20, 31, 39, 40, 41]<br>8. [2, 4, 10, 11, 16, 18]<br>9. [16, 19, 27, 29, 31, 39]<br>10. [7, 27, 28, 29, 30, 35]<br>11. [1, 5, 14, 23, 25, 43]<br>12. [1, 17, 19, 28, 32, 42]<br>13. [2, 12, 23, 31, 34, 42]<br>14. [4, 11, 24, 34, 36, 45]<br>15. [1, 5, 12, 16, 19, 24]<br>16. [8, 13, 20, 22, 31, 41]<br>17. [3, 15, 19, 26, 35, 36]<br>18. [17, 18, 28, 35, 43, 44]<br>19. [7, 11, 25, 29, 35, 40]<br>20. [4, 8, 22, 28, 29, 33]<br>21. [1, 14, 26, 27, 30, 34]<br>22. [2, 13, 28, 32, 37, 41]<br>23. [20, 24, 31, 38, 42, 44]<br>24. [3, 4, 21, 30, 35, 44]<br>25. [2, 16, 24, 30, 42, 44]<br>26. [8, 20, 24, 28, 30, 41]<br>27. [2, 23, 29, 30, 43, 45]<br>28. [10, 15, 24, 32, 41, 42]<br>29. [19, 22, 24, 25, 26, 30]<br>30. [1, 6, 29, 36, 37, 45]<br>31. [4, 8, 24, 27, 37, 39]<br>32. [3, 15, 20, 27, 35, 38]<br>33. [11, 12, 16, 21, 26, 38] |
| Chiến lược Suy giảm Exponential | 5 số (2022-07-08, giải 5,000tr) | 45, 44, 43, 23, 22, 17 | 1 | 1. [1, 10, 20, 23, 35, 43] |
| Chiến lược Không Lặp lại | 4 số (2026-03-06, giải 0.5tr) | 41, 39, 30, 27, 5, 3 | 1 | 1. [3, 5, 27, 30, 39, 41] |
| Chiến lược Mẫu | 4 số (2026-02-27, giải 0.5tr) | 35, 29, 16, 8, 5, 2 | 1 | 1. [5, 6, 7, 11, 18, 40] |
| Chiến lược Số Nóng | 4 số (2026-02-06, giải 0.5tr) | 42, 28, 14, 13, 10, 7 | 1 | 1. [7, 9, 12, 21, 24, 28] |
| Chiến lược Vắng mặt Lâu dài | 4 số (2026-03-06, giải 0.5tr) | 41, 39, 17, 9, 3, 1 | 1 | 1. [1, 3, 9, 24, 27, 39] |
| Chiến lược Số Lạnh | 5 số (2022-10-19, giải 5,000tr) | 41, 40, 33, 9, 5, 3 | 1 | 1. [1, 12, 16, 19, 30, 34] |
| Chiến lược Tần suất Cặp | 5 số (2025-05-07, giải 5,000tr) | 45, 43, 42, 28, 7, 2 | 1 | 1. [13, 14, 32, 42, 43, 44] |


## 🧪 Đánh giá Rolling Out-of-Sample

> Cửa sổ kiểm thử ngoài mẫu: **60 ngày gần nhất (tự động chọn)** (đến 2026-03-20).
> Mục tiêu: đánh giá chiến lược trên giai đoạn gần đây, giảm thiên lệch do fit vào toàn bộ lịch sử.

| Chiến lược | Giai đoạn OOS | Tài chính OOS | Phân bố trùng khớp OOS |
|------------|----------------|---------------|--------------------------|
| Chiến lược Ngẫu nhiên | 2026-01-21 00:00:00 → 2026-03-20 00:00:00 (520 dự đoán) | chi 5.2tr, lợi 5,001.6tr, roi 96085.58% | 6+: 0, 5: 1, 4: 2, 3: 13 |
| Chiến lược Suy giảm Exponential | 2026-01-21 00:00:00 → 2026-03-20 00:00:00 (520 dự đoán) | chi 5.2tr, lợi 1.8tr, roi -66.35% | 6+: 0, 5: 0, 4: 2, 3: 15 |
| Chiến lược Không Lặp lại | 2026-01-21 00:00:00 → 2026-03-20 00:00:00 (520 dự đoán) | chi 5.2tr, lợi 1.2tr, roi -76.92% | 6+: 0, 5: 0, 4: 2, 3: 4 |
| Chiến lược Mẫu | 2026-01-21 00:00:00 → 2026-03-20 00:00:00 (520 dự đoán) | chi 5.2tr, lợi 1.1tr, roi -79.81% | 6+: 0, 5: 0, 4: 1, 3: 11 |
| Chiến lược Số Nóng | 2026-01-21 00:00:00 → 2026-03-20 00:00:00 (520 dự đoán) | chi 5.2tr, lợi 1tr, roi -80.77% | 6+: 0, 5: 0, 4: 1, 3: 10 |
| Chiến lược Vắng mặt Lâu dài | 2026-01-21 00:00:00 → 2026-03-20 00:00:00 (520 dự đoán) | chi 5.2tr, lợi 0.8tr, roi -85.58% | 6+: 0, 5: 0, 4: 1, 3: 5 |
| Chiến lược Số Lạnh | 2026-01-21 00:00:00 → 2026-03-20 00:00:00 (520 dự đoán) | chi 5.2tr, lợi 0.7tr, roi -87.50% | 6+: 0, 5: 0, 4: 0, 3: 13 |
| Chiến lược Tần suất Cặp | 2026-01-21 00:00:00 → 2026-03-20 00:00:00 (520 dự đoán) | chi 5.2tr, lợi 0.5tr, roi -90.38% | 6+: 0, 5: 0, 4: 0, 3: 10 |




## 🧾 Leaderboard Lịch sử

> Tổng hợp từ **21 bản ghi gần nhất** của sản phẩm `power_645`.
> Bảng này giúp ưu tiên chiến lược ổn định theo thời gian, không chỉ theo một lần chạy.

| Hạng | Chiến lược | ROI TB lịch sử | ROI Độ lệch chuẩn | Số run |
|------|------------|----------------|-------------------|--------|
| 1 | Chiến lược Ngẫu nhiên | 2462.30% | 2128.78% | 43 |
| 2 | Chiến lược Suy giảm Exponential | 1875.71% | 1493.43% | 43 |
| 3 | Chiến lược Số Lạnh | 1758.07% | 1531.37% | 43 |
| 4 | Chiến lược Mẫu | 1523.56% | 1306.22% | 43 |
| 5 | Chiến lược Số Nóng | 1170.38% | 966.52% | 43 |
| 6 | Chiến lược Vắng mặt Lâu dài | 1169.54% | 895.81% | 43 |
| 7 | Chiến lược Tần suất Cặp | 701.20% | 1167.07% | 43 |
| 8 | Chiến lược Không Lặp lại | -79.62% | 0.62% | 43 |


---

## ⚠️ Tuyên bố Miễn trách nhiệm

Tóm tắt dự đoán này chỉ dành cho mục đích giáo dục và nghiên cứu. Kết quả xổ số ngẫu nhiên và không thể dự đoán một cách đáng tin cậy. Không bao giờ cờ bạc nhiều hơn những gì bạn có thể mất được.
