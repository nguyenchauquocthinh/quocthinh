import streamlit as st
from PIL import Image
import base64

# Cài đặt giao diện
st.set_page_config(layout="wide", page_title="Free Fire UI", page_icon="🔥")

# CSS nền và giao diện
def set_bg(image_path):
    with open(image_path, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
        }}
        .center {{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 80vh;
            flex-direction: column;
        }}
        .button-big {{
            background-color: gold;
            color: black;
            font-size: 24px;
            padding: 14px 30px;
            border-radius: 10px;
            border: none;
            font-weight: bold;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg("freefire_bg.png")

# Layout chia 3 cột
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.markdown("### 📦 SHOP")
    st.markdown("### 🎡 VÒNG QUAY")
    st.markdown("### 🧍 NHÂN VẬT")
    st.markdown("### 🎒 TỦ ĐỒ")
    st.markdown("### 🐶 TRỢ THỦ")
    st.markdown("### 🔫 VŨ KHÍ")

with col2:
    st.markdown('<div class="center"><h2 style="color:white">🔥 Nhân Vật Chính 🔥</h2><img src="https://i.imgur.com/3VQWmZj.png" width="220"></div>', unsafe_allow_html=True)

with col3:
    st.markdown("#### ⚙️ Cài đặt")
    st.markdown("#### 📬 Thư")
    st.markdown("#### 👥 Bạn bè")
    st.markdown("#### 🛡️ Xếp hạng")

    st.markdown("---")
    st.markdown('<div style="text-align:center;"><button class="button-big">BẮT ĐẦU</button></div>', unsafe_allow_html=True)


