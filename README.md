# Ứng dụng Nhận Diện Cảm Xúc từ Phản Hồi của Sinh Viên

## Giới thiệu

Ứng dụng này được phát triển để nhận diện cảm xúc từ các phản hồi của sinh viên. Việc này có thể hữu ích trong việc đánh giá sự hài lòng, mức độ thích thú hoặc các cảm xúc khác của sinh viên đối với một dịch vụ hoặc sản phẩm cụ thể.

Ứng dụng sử dụng mô hình học máy đã được đào tạo trước và một vectorizer để chuyển đổi văn bản thành dạng thích hợp cho việc dự đoán cảm xúc.

## Cách Sử Dụng

1. **Nhập Phản Hồi**: Nhập phản hồi từ sinh viên vào ô văn bản.

2. **Dự Đoán Cảm Xúc**: Nhấn vào nút "Dự đoán cảm xúc" để xem kết quả.

3. **Xem Kết Quả**: Kết quả sẽ hiển thị với một trong ba nhãn cảm xúc: Tích cực, Trung tính hoặc Tiêu cực.

## Cài Đặt và Chạy

1. **Cài Đặt Streamlit**: Đảm bảo bạn đã cài đặt thư viện Streamlit. Nếu chưa, bạn có thể cài đặt bằng cách sử dụng pip:

    ```
    pip install streamlit
    ```

2. **Tải Dữ Liệu và Mô Hình**: Đảm bảo rằng bạn đã tải dữ liệu và mô hình cần thiết cho ứng dụng. Các tệp tin cần được đặt trong cùng thư mục với script Python (`app.py`). Trong trường hợp này, cần tải:

    - Tệp tin `svm_model.pkl`: Mô hình máy học đã được đào tạo.
    - Tệp tin `tf_idf.pkl`: Vectorizer được sử dụng để chuyển đổi văn bản thành dạng thích hợp.

3. **Chạy Ứng Dụng**: Mở terminal, di chuyển đến thư mục chứa script Python và chạy lệnh:

    ```
    streamlit run app.py
    ```

4. **Sử Dụng Ứng Dụng**: Một cửa sổ trình duyệt mới sẽ mở và hiển thị giao diện người dùng của ứng dụng. Bạn có thể nhập phản hồi và nhấn nút để dự đoán cảm xúc.

## Yêu Cầu

- Python 3.x
- Streamlit
- scikit-learn
- pyvi

