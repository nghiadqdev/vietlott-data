# 🔮 Tóm tắt Dự đoán Vietlott Power 645

> **Được tạo**: 2026-04-10 17:24:25
> **Seed**: ngẫu nhiên, **Seed runs**: 1
>
>
> Tài liệu này chứa các dự đoán học máy cho dữ liệu xổ số Việt Nam.
    > Đây là một mô-đun thử nghiệm chỉ dành cho mục đích giáo dục.
    > ROI cao trong báo cáo chủ yếu là kết quả backtest/OOS; thực tế các kỳ quay gần vẫn có thể chỉ trùng 0-2 số.

## 📊 So sánh Hiệu suất Chiến lược

> Sắp xếp theo ROI (tốt nhất → tệ nhất). Tất cả các chiến lược được kiểm thử với **20 vé/lần quay**.
> Lưu ý: Tất cả ROI đều âm sâu — xác suất xổ số khiến lợi nhuận không thể xảy ra ở quy mô lớn.
> So sánh cho thấy *chiến lược nào thua ít nhất*, không phải chiến lược nào có lợi.

| Hạng | Chiến lược | Tổng Chi phí (tr) | Tổng Lợi nhuận (tr) | Lợi nhuận ròng (tr) | ROI |
|------|----------|-----------------|-----------------|-----------------|-----|
| 🥇 1 | Chiến lược Tần suất Cặp | 297.2tr | 10,053.6tr | 9,756.4tr | 3282.77% |
| 🥈 2 | Chiến lược Vắng mặt Lâu dài | 297.2tr | 10,052.3tr | 9,755.1tr | 3282.34% |
| 🥉 3 | Chiến lược Mẫu | 297.2tr | 10,049.2tr | 9,752tr | 3281.31% |
|    4 | Chiến lược Suy giảm Exponential | 297.2tr | 5,053.6tr | 4,756.4tr | 1600.39% |
|    5 | Chiến lược Không Lặp lại | 297.2tr | 60.3tr | -236.9tr | -79.71% |
|    6 | Chiến lược Số Nóng | 297.2tr | 54.6tr | -242.6tr | -81.61% |
|    7 | Chiến lược Số Lạnh | 297.2tr | 54tr | -243.2tr | -81.85% |
|    8 | Chiến lược Ngẫu nhiên | 297.2tr | 52.5tr | -244.7tr | -82.32% |


## 📊 So sánh ROI: Benchmark vs Khung nhớ động

    > Bảng A là benchmark cố định trên toàn bộ lịch sử.
    > Bảng B là ROI ở cửa sổ gần đây **540 ngày gần nhất (tự động chọn)** để mô phỏng vận hành động.
    > Cột **ΔROI** giúp bạn thấy mức thay đổi khi chuyển từ khung nhớ cố định sang khung nhớ gần.
    > Lưu ý: ROI cao ở đây vẫn chỉ là thước đo backtest/OOS, không có nghĩa là vài kỳ quay gần nhất sẽ trùng nhiều số hơn.

### Bảng A: ROI Benchmark (Toàn kỳ)

| Hạng | Chiến lược | Tổng Chi phí (tr) | Tổng Lợi nhuận (tr) | Lợi nhuận ròng (tr) | ROI Toàn kỳ |
|------|------------|-------------------|---------------------|---------------------|-------------|
| 🥇 1 | Chiến lược Tần suất Cặp | 297.2tr | 10,053.6tr | 9,756.4tr | 3282.77% |
| 🥈 2 | Chiến lược Vắng mặt Lâu dài | 297.2tr | 10,052.3tr | 9,755.1tr | 3282.34% |
| 🥉 3 | Chiến lược Mẫu | 297.2tr | 10,049.2tr | 9,752tr | 3281.31% |
|    4 | Chiến lược Suy giảm Exponential | 297.2tr | 5,053.6tr | 4,756.4tr | 1600.39% |
|    5 | Chiến lược Không Lặp lại | 297.2tr | 60.3tr | -236.9tr | -79.71% |
|    6 | Chiến lược Số Nóng | 297.2tr | 54.6tr | -242.6tr | -81.61% |
|    7 | Chiến lược Số Lạnh | 297.2tr | 54tr | -243.2tr | -81.85% |
|    8 | Chiến lược Ngẫu nhiên | 297.2tr | 52.5tr | -244.7tr | -82.32% |

### Bảng B: ROI Khung nhớ động (OOS gần đây)

| Hạng | Chiến lược | Chi phí OOS (tr) | Lợi nhuận OOS (tr) | ROI OOS | ΔROI (OOS - Toàn kỳ) |
|------|------------|------------------|--------------------|---------|-----------------------|
| 🥇 1 | Chiến lược Tần suất Cặp | 46.2tr | 10,010.4tr | 21567.53% | +18284.76% |
| 🥈 2 | Chiến lược Mẫu | 46.2tr | 10,007.2tr | 21560.71% | +18279.41% |
| 🥉 3 | Chiến lược Không Lặp lại | 46.2tr | 13.8tr | -70.13% | +9.58% |
|    4 | Chiến lược Suy giảm Exponential | 46.2tr | 11.2tr | -75.76% | -1676.14% |
|    5 | Chiến lược Số Lạnh | 46.2tr | 9tr | -80.52% | +1.33% |
|    6 | Chiến lược Số Nóng | 46.2tr | 8.6tr | -81.39% | +0.23% |
|    7 | Chiến lược Ngẫu nhiên | 46.2tr | 8.3tr | -82.03% | +0.28% |
|    8 | Chiến lược Vắng mặt Lâu dài | 46.2tr | 7.2tr | -84.31% | -3366.64% |


## 📉 Biểu đồ ROI Tổng quát

> Biểu đồ thanh tương đối để nhìn nhanh chiến lược nào đang trội/yếu trong lần chạy hiện tại.
> Dấu '+' là ROI dương, dấu '-' là ROI âm. Độ dài thanh được chuẩn hóa theo giá trị tuyệt đối lớn nhất.

| Chiến lược | ROI | Biểu đồ tương đối |
|------------|-----|-------------------|
| Chiến lược Tần suất Cặp | 3282.77% | ++++++++++++++++++++++++ |
| Chiến lược Vắng mặt Lâu dài | 3282.34% | +++++++++++++++++++++++ |
| Chiến lược Mẫu | 3281.31% | +++++++++++++++++++++++ |
| Chiến lược Suy giảm Exponential | 1600.39% | +++++++++++ |
| Chiến lược Không Lặp lại | -79.71% | - |
| Chiến lược Số Nóng | -81.61% | - |
| Chiến lược Số Lạnh | -81.85% | - |
| Chiến lược Ngẫu nhiên | -82.32% | - |


## 📋 Bảng Chiến lược Tóm tắt

    > Ngày dự đoán: **2026-03-22**.
    > Bảng rút gọn: chỉ giữ các chỉ số quan trọng để dễ so sánh nhanh.
    > ROI ở đây phản ánh hiệu quả trên dữ liệu lịch sử và OOS, không phải xác suất trúng cao ở các kỳ quay sắp tới.

| Chiến lược | ROI | Tóm tắt Tài chính | Giải cao nhất (kỳ gần nhất) | Phân bố Trùng khớp | 6 Hàng đầu |
|----------|-----|-------------------|-----------------------------|--------------------|--------|
| Chiến lược Tần suất Cặp | 3282.77% | chi 297.2tr, lợi 10,053.6tr, roi 3282.77% | 5 số (2025-06-15, giải 5,000tr) | 5+: 2, 4: 40, 3: 672 | 28, 7, 22, 29, 13, 26 |
| Chiến lược Vắng mặt Lâu dài | 3282.34% | chi 297.2tr, lợi 10,052.3tr, roi 3282.34% | 5 số (2024-04-28, giải 5,000tr) | 5+: 2, 4: 40, 3: 646 | 24, 40, 30, 45, 41, 1 |
| Chiến lược Mẫu | 3281.31% | chi 297.2tr, lợi 10,049.2tr, roi 3281.31% | 5 số (2025-12-03, giải 5,000tr) | 5+: 2, 4: 28, 3: 705 | 5, 23, 16, 6, 25, 4 |
| Chiến lược Suy giảm Exponential | 1600.39% | chi 297.2tr, lợi 5,053.6tr, roi 1600.39% | 5 số (2020-03-27, giải 5,000tr) | 5+: 1, 4: 45, 3: 621 | 31, 23, 42, 44, 45, 38 |
| Chiến lược Không Lặp lại | -79.71% | chi 297.2tr, lợi 60.3tr, roi -79.71% | 4 số (2025-12-26, giải 0.5tr) | 5+: 0, 4: 67, 3: 536 | 3, 5, 27, 30, 39, 41 |
| Chiến lược Số Nóng | -81.61% | chi 297.2tr, lợi 54.6tr, roi -81.61% | 4 số (2025-12-31, giải 0.5tr) | 5+: 0, 4: 40, 3: 693 | 22, 42, 31, 24, 44, 45 |
| Chiến lược Số Lạnh | -81.85% | chi 297.2tr, lợi 54tr, roi -81.85% | 4 số (2026-02-08, giải 0.5tr) | 5+: 0, 4: 40, 3: 679 | 40, 33, 3, 16, 38, 25 |
| Chiến lược Ngẫu nhiên | -82.32% | chi 297.2tr, lợi 52.5tr, roi -82.32% | 4 số (2026-02-15, giải 0.5tr) | 5+: 0, 4: 36, 3: 691 | 1, 35, 43, 42, 26, 30 |


## 🎯 So sánh Trùng khớp Với Kỳ trước

> Bảng này chỉ hiển thị lại kết quả đã chạy trước đó (kỳ gần nhất trong tập evaluate của từng chiến lược).
> Các số trùng giữa bộ số chiến lược và kết quả trúng kỳ trước được tô **đỏ** để dễ nhìn.

| Chiến lược | Kỳ trước | Bộ số chiến lược (số trùng màu đỏ) | Kết quả trúng kỳ trước (số trùng màu đỏ) | Số trùng |
|------------|----------|-------------------------------------|-------------------------------------------|----------|
| Chiến lược Không Lặp lại | 2026-03-20 00:00:00 | 5, 27, 30, 39, 41, <span style='color:#d00000;font-weight:700'>43</span> | 8, 11, 22, 23, 38, <span style='color:#d00000;font-weight:700'>43</span> | 1 |
| Chiến lược Ngẫu nhiên | 2026-03-20 00:00:00 | 1, 20, 33, 37, 41, 44 | 8, 11, 22, 23, 38, 43 | 0 |
| Chiến lược Vắng mặt Lâu dài | 2026-03-20 00:00:00 | 3, 15, 24, 30, 39, 40 | 8, 11, 22, 23, 38, 43 | 0 |
| Chiến lược Mẫu | 2026-03-20 00:00:00 | 6, 17, 28, 29, 32, 36 | 8, 11, 22, 23, 38, 43 | 0 |
| Chiến lược Số Nóng | 2026-03-20 00:00:00 | 7, 10, 20, 26, 27, 45 | 8, 11, 22, 23, 38, 43 | 0 |
| Chiến lược Số Lạnh | 2026-03-20 00:00:00 | 4, 10, 12, 16, 28, 39 | 8, 11, 22, 23, 38, 43 | 0 |
| Chiến lược Suy giảm Exponential | 2026-03-20 00:00:00 | 15, 16, 17, 25, 29, 40 | 8, 11, 22, 23, 38, 43 | 0 |
| Chiến lược Tần suất Cặp | 2026-03-20 00:00:00 | 1, 3, 9, 35, 40, 44 | 8, 11, 22, 23, 38, 43 | 0 |


## 🔭 Dự đoán Số cho Lần Quay Tiếp theo

> Dự đoán cho lần quay tiếp theo vào: **2026-03-22**.
> Phương pháp: mỗi chiến lược mô phỏng **200** vé, sau đó tất cả vé được tổng hợp.
> Đây là xếp hạng xác suất, không phải các số trúng đảm bảo.

### Bảng A - 6 số ứng cử viên theo Toàn kỳ

| Số | Điểm Tập hợp | Xuất hiện trong Vé |
|--------|----------------|---------------------|
| 41 | 454 | 28.38% |
| 30 | 454 | 28.38% |
| 27 | 429 | 26.81% |
| 3 | 426 | 26.62% |
| 39 | 422 | 26.38% |
| 5 | 411 | 25.69% |

### Bảng B - 6 số ứng cử viên theo Khung nhớ động

> Trọng số chiến lược được tính theo ROI OOS trong **540 ngày gần nhất (tự động chọn)**.
> Phân bổ số bộ/chiến lược: **động theo ROI OOS (tổng 40 bộ)**.

| Số | Điểm Động (weighted) | Tỷ trọng Điểm Động |
|--------|-----------------------|--------------------|
| 10 | 1466490.1 | 2.83% |
| 4 | 1444882.9 | 2.79% |
| 29 | 1423475.3 | 2.75% |
| 22 | 1423417.4 | 2.75% |
| 36 | 1401801.9 | 2.71% |
| 35 | 1401748.8 | 2.71% |

### 6 hàng đầu theo Chiến lược - Bảng A (xếp theo ROI Toàn kỳ)

| Chiến lược | Giải cao nhất (kỳ gần nhất) | Số hàng đầu | x bộ số | Danh sách bộ số gợi ý |
|----------|-----------------------------|-------------|--------|------------------------|
| Chiến lược Tần suất Cặp | 5 số (2025-06-15, giải 5,000tr) | 45, 42, 34, 28, 22, 7 | 17 | 1. [8, 19, 21, 27, 37, 42]<br>2. [7, 12, 15, 29, 33, 34]<br>3. [5, 8, 22, 28, 35, 37]<br>4. [5, 8, 10, 27, 28, 32]<br>5. [24, 26, 29, 36, 37, 41]<br>6. [4, 9, 11, 22, 40, 43]<br>7. [7, 8, 18, 25, 26, 31]<br>8. [12, 21, 28, 30, 34, 38]<br>9. [24, 25, 28, 30, 43, 44]<br>10. [1, 3, 16, 22, 28, 43]<br>11. [2, 4, 16, 18, 28, 40]<br>12. [4, 15, 19, 28, 35, 43]<br>13. [4, 23, 30, 33, 34, 39]<br>14. [8, 9, 11, 24, 34, 45]<br>15. [7, 20, 30, 31, 35, 43]<br>16. [5, 6, 18, 19, 30, 40]<br>17. [4, 17, 20, 29, 31, 34] |
| Chiến lược Vắng mặt Lâu dài | 5 số (2024-04-28, giải 5,000tr) | 41, 40, 39, 29, 15, 9 | 1 | 1. [1, 17, 29, 34, 39, 40] |
| Chiến lược Mẫu | 5 số (2025-12-03, giải 5,000tr) | 36, 35, 11, 10, 4, 2 | 17 | 1. [3, 9, 10, 20, 37, 43]<br>2. [4, 9, 26, 27, 28, 37]<br>3. [5, 6, 16, 33, 34, 35]<br>4. [18, 19, 21, 33, 34, 44]<br>5. [2, 15, 16, 17, 36, 43]<br>6. [3, 7, 25, 26, 28, 29]<br>7. [15, 27, 28, 31, 34, 43]<br>8. [15, 18, 24, 25, 26, 41]<br>9. [6, 13, 18, 19, 20, 27]<br>10. [7, 11, 15, 30, 37, 40]<br>11. [5, 9, 11, 25, 32, 45]<br>12. [2, 3, 6, 13, 19, 40]<br>13. [10, 13, 25, 26, 27, 40]<br>14. [26, 31, 35, 36, 38, 40]<br>15. [4, 7, 8, 20, 33, 35]<br>16. [10, 12, 18, 24, 32, 41]<br>17. [7, 8, 14, 15, 27, 40] |
| Chiến lược Suy giảm Exponential | 5 số (2020-03-27, giải 5,000tr) | 43, 42, 36, 31, 23, 20 | 1 | 1. [5, 14, 16, 31, 41, 42] |
| Chiến lược Không Lặp lại | 4 số (2025-12-26, giải 0.5tr) | 41, 39, 30, 27, 5, 3 | 1 | 1. [3, 5, 27, 30, 39, 41] |
| Chiến lược Số Nóng | 4 số (2025-12-31, giải 0.5tr) | 44, 34, 31, 28, 14, 7 | 1 | 1. [2, 20, 29, 30, 35, 41] |
| Chiến lược Số Lạnh | 4 số (2026-02-08, giải 0.5tr) | 41, 40, 33, 21, 19, 3 | 1 | 1. [1, 3, 16, 23, 29, 40] |
| Chiến lược Ngẫu nhiên | 4 số (2026-02-15, giải 0.5tr) | 45, 44, 43, 41, 19, 16 | 1 | 1. [8, 12, 14, 15, 23, 35] |

### 6 hàng đầu theo Chiến lược - Bảng B (xếp theo ROI Khung nhớ động)

> Xếp hạng theo ROI OOS trong **540 ngày gần nhất (tự động chọn)**.

| Chiến lược | Giải cao nhất (kỳ gần nhất) | Số hàng đầu | x bộ số | Danh sách bộ số gợi ý |
|----------|-----------------------------|-------------|--------|------------------------|
| Chiến lược Tần suất Cặp | 5 số (2025-06-15, giải 5,000tr) | 45, 42, 34, 28, 22, 7 | 17 | 1. [7, 11, 26, 27, 30, 39]<br>2. [7, 8, 10, 20, 23, 28]<br>3. [1, 6, 13, 19, 37, 42]<br>4. [2, 4, 6, 18, 30, 39]<br>5. [8, 10, 14, 15, 22, 23]<br>6. [3, 9, 21, 35, 42, 43]<br>7. [8, 11, 13, 20, 36, 39]<br>8. [26, 30, 31, 32, 37, 38]<br>9. [16, 18, 19, 20, 38, 44]<br>10. [4, 5, 14, 17, 28, 39]<br>11. [2, 17, 32, 33, 38, 44]<br>12. [1, 2, 14, 22, 24, 26]<br>13. [3, 8, 10, 26, 29, 32]<br>14. [5, 15, 26, 28, 36, 43]<br>15. [4, 5, 6, 17, 28, 44]<br>16. [7, 29, 31, 32, 40, 44]<br>17. [5, 15, 17, 22, 26, 39] |
| Chiến lược Mẫu | 5 số (2025-12-03, giải 5,000tr) | 36, 35, 11, 10, 4, 2 | 17 | 1. [6, 12, 14, 21, 30, 32]<br>2. [4, 12, 17, 20, 21, 34]<br>3. [2, 4, 5, 12, 24, 37]<br>4. [6, 22, 26, 32, 33, 34]<br>5. [28, 32, 34, 36, 40, 45]<br>6. [18, 27, 28, 30, 31, 36]<br>7. [6, 9, 10, 12, 40, 41]<br>8. [6, 18, 24, 26, 31, 34]<br>9. [7, 11, 13, 14, 21, 33]<br>10. [15, 16, 17, 32, 33, 36]<br>11. [1, 2, 7, 9, 40, 41]<br>12. [18, 20, 21, 22, 24, 42]<br>13. [16, 24, 26, 28, 34, 39]<br>14. [7, 10, 16, 22, 32, 37]<br>15. [6, 12, 13, 34, 35, 36]<br>16. [5, 25, 32, 34, 35, 38]<br>17. [7, 13, 17, 24, 28, 34] |
| Chiến lược Không Lặp lại | 4 số (2025-12-26, giải 0.5tr) | 41, 39, 30, 27, 5, 3 | 1 | 1. [3, 5, 27, 30, 39, 41] |
| Chiến lược Suy giảm Exponential | 5 số (2020-03-27, giải 5,000tr) | 43, 42, 36, 31, 23, 20 | 1 | 1. [16, 19, 24, 25, 32, 37] |
| Chiến lược Số Lạnh | 4 số (2026-02-08, giải 0.5tr) | 41, 40, 33, 21, 19, 3 | 1 | 1. [1, 15, 20, 23, 35, 39] |
| Chiến lược Số Nóng | 4 số (2025-12-31, giải 0.5tr) | 44, 34, 31, 28, 14, 7 | 1 | 1. [13, 18, 26, 35, 39, 43] |
| Chiến lược Ngẫu nhiên | 4 số (2026-02-15, giải 0.5tr) | 45, 44, 43, 41, 19, 16 | 1 | 1. [8, 9, 14, 18, 30, 38] |
| Chiến lược Vắng mặt Lâu dài | 5 số (2024-04-28, giải 5,000tr) | 41, 40, 39, 29, 15, 9 | 1 | 1. [1, 3, 17, 29, 34, 45] |


## 🧪 Đánh giá Rolling Out-of-Sample

> Cửa sổ kiểm thử ngoài mẫu: **540 ngày gần nhất (tự động chọn)** (đến 2026-03-20).
> Mục tiêu: đánh giá chiến lược trên giai đoạn gần đây, giảm thiên lệch do fit vào toàn bộ lịch sử.

| Chiến lược | Giai đoạn OOS | Tài chính OOS | Phân bố trùng khớp OOS |
|------------|----------------|---------------|--------------------------|
| Chiến lược Tần suất Cặp | 2024-09-27 00:00:00 → 2026-03-20 00:00:00 (4,620 dự đoán) | chi 46.2tr, lợi 10,010.4tr, roi 21567.53% | 6+: 0, 5: 2, 4: 11, 3: 98 |
| Chiến lược Mẫu | 2024-09-27 00:00:00 → 2026-03-20 00:00:00 (4,620 dự đoán) | chi 46.2tr, lợi 10,007.2tr, roi 21560.71% | 6+: 0, 5: 2, 4: 4, 3: 105 |
| Chiến lược Không Lặp lại | 2024-09-27 00:00:00 → 2026-03-20 00:00:00 (4,620 dự đoán) | chi 46.2tr, lợi 13.8tr, roi -70.13% | 6+: 0, 5: 0, 4: 21, 3: 66 |
| Chiến lược Suy giảm Exponential | 2024-09-27 00:00:00 → 2026-03-20 00:00:00 (4,620 dự đoán) | chi 46.2tr, lợi 11.2tr, roi -75.76% | 6+: 0, 5: 0, 4: 12, 3: 104 |
| Chiến lược Số Lạnh | 2024-09-27 00:00:00 → 2026-03-20 00:00:00 (4,620 dự đoán) | chi 46.2tr, lợi 9tr, roi -80.52% | 6+: 0, 5: 0, 4: 9, 3: 90 |
| Chiến lược Số Nóng | 2024-09-27 00:00:00 → 2026-03-20 00:00:00 (4,620 dự đoán) | chi 46.2tr, lợi 8.6tr, roi -81.39% | 6+: 0, 5: 0, 4: 7, 3: 102 |
| Chiến lược Ngẫu nhiên | 2024-09-27 00:00:00 → 2026-03-20 00:00:00 (4,620 dự đoán) | chi 46.2tr, lợi 8.3tr, roi -82.03% | 6+: 0, 5: 0, 4: 5, 3: 116 |
| Chiến lược Vắng mặt Lâu dài | 2024-09-27 00:00:00 → 2026-03-20 00:00:00 (4,620 dự đoán) | chi 46.2tr, lợi 7.2tr, roi -84.31% | 6+: 0, 5: 0, 4: 6, 3: 85 |




## 🧾 Leaderboard Lịch sử

> Tổng hợp từ **25 bản ghi gần nhất** của sản phẩm `power_645`.
> Bảng này giúp ưu tiên chiến lược ổn định theo thời gian, không chỉ theo một lần chạy.

| Hạng | Chiến lược | ROI TB lịch sử | ROI Độ lệch chuẩn | Số run |
|------|------------|----------------|-------------------|--------|
| 1 | Chiến lược Ngẫu nhiên | 2353.11% | 2107.08% | 47 |
| 2 | Chiến lược Số Lạnh | 1780.48% | 1481.89% | 47 |
| 3 | Chiến lược Suy giảm Exponential | 1744.89% | 1506.53% | 47 |
| 4 | Chiến lược Mẫu | 1530.03% | 1386.58% | 47 |
| 5 | Chiến lược Số Nóng | 1171.08% | 1010.07% | 47 |
| 6 | Chiến lược Vắng mặt Lâu dài | 1170.31% | 882.87% | 47 |
| 7 | Chiến lược Tần suất Cặp | 1064.03% | 2224.75% | 47 |
| 8 | Chiến lược Không Lặp lại | -79.69% | 0.65% | 47 |


---

## ⚠️ Tuyên bố Miễn trách nhiệm

Tóm tắt dự đoán này chỉ dành cho mục đích giáo dục và nghiên cứu. Kết quả xổ số ngẫu nhiên và không thể dự đoán một cách đáng tin cậy. Không bao giờ cờ bạc nhiều hơn những gì bạn có thể mất được.
