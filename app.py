import pandas as pd
import streamlit as st

st.title("🔖 Tạo mã sản phẩm ASUS")

uploaded_file = st.file_uploader("Upload file Excel", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    # Giả sử file có các cột: Model, CPU, RAM, SSD, Screen, WiFi, BT, Pin, OS, Color
    def tao_ma_sp(row):
        return f"(NB) ASUS {row['Model']} {row['CPU']}/{row['RAM']}/{row['SSD']}/{row['Screen']}/{row['WiFi']}/{row['BT']}/{row['Pin']}/{row['OS']}/{row['Color']}"

    df["Mã sản phẩm"] = df.apply(tao_ma_sp, axis=1)

    st.success("✅ Đã tạo mã sản phẩm")

    # Hiển thị bảng
    st.dataframe(df)

    # Xuất ra Excel
    output_file = "ma_san_pham.xlsx"
    df.to_excel(output_file, index=False)

    with open(output_file, "rb") as f:
        st.download_button("⬇️ Tải file kết quả", f, file_name="ma_san_pham.xlsx")