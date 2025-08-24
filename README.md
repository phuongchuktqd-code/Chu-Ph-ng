# ASUS Product Code Generator

Web app tạo mã sản phẩm ASUS từ file Excel bằng Python + Streamlit.

## Hướng dẫn sử dụng

1. Upload file Excel (chứa các cột: Model, CPU, RAM, SSD, Screen, WiFi, BT, Pin, OS, Color).
2. App sẽ tự động sinh mã sản phẩm theo cấu trúc chuẩn.
3. Download file kết quả đã có cột "Mã sản phẩm".

## Chạy thử local

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy lên Streamlit Community Cloud

1. Đưa toàn bộ code này lên GitHub
2. Kết nối repo với https://streamlit.io/cloud
3. Chọn file `app.py` để deploy
