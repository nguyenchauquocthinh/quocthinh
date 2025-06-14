import streamlit as st
import base64

st.set_page_config(layout="wide", page_title="Free Fire UI", page_icon="🔥")

# Đọc ảnh nền
def set_bg(image_file):
    with open(image_file, "rb") as f:
        data = base64.b64encode(f.read()).decode()
    bg_style = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{data}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    .button-big {{
        background-color: gold;
        color: black;
        font-size: 24px;
        padding: 14px 30px;
        border-radius: 10px;
        border: none;
        font-weight: bold;
        text-align: center;
    }}
    </style>
    """
    st.markdown(bg_style, unsafe_allow_html=True)

# ✅ Sửa đường dẫn đúng với file bạn vừa tải lên
set_bg("/mnt/data/0a0f4242-2f0a-44b0-a56a-eb057f681079.png")

# Layout
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.markdown("### 📦 SHOP")
    st.markdown("### 🎡 VÒNG QUAY")
    st.markdown("### 🧍 NHÂN VẬT")
    st.markdown("### 🎒 TỦ ĐỒ")
    st.markdown("### 🐶 TRỢ THỦ")
    st.markdown("### 🔫 VŨ KHÍ")

with col2:
    st.markdown(
        """
        <div style="text-align: center;">
            <h2 style="color:white">🔥 Nhân Vật Chính 🔥</h2>
            <img src="https://i.imgur.com/3VQWmZj.png" width="220">
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown("#### ⚙️ Cài đặt")
    st.markdown("#### 📬 Thư")
    st.markdown("#### 👥 Bạn bè")
    st.markdown("#### 🛡️ Xếp hạng")
    st.markdown("---")
    st.markdown('<div style="text-align:center;"><button class="button-big">BẮT ĐẦU</button></div>', unsafe_allow_html=True)



