import streamlit as st
import time

# Tạo một dictionary lưu thông tin user
USER_CREDENTIALS = {
    "admin": "123456",
    "user": "abc123"
}

# Thiết lập giao diện
st.set_page_config(page_title="Đăng nhập", page_icon="🔐", layout="centered")

# Hiệu ứng login
def login_animation():
    with st.spinner('Đang kiểm tra thông tin...'):
        time.sleep(1.5)

# Trang chính sau khi đăng nhập thành công
def main_page(username):
    st.success(f"🎉 Xin chào {username}, bạn đã đăng nhập thành công!")
    st.balloons()
    st.write("Chào mừng bạn đến với hệ thống!")

# Giao diện đăng nhập
def login_page():
    st.markdown("## 🔐 Đăng Nhập Hệ Thống")
    username = st.text_input("👤 Tên đăng nhập")
    password = st.text_input("🔑 Mật khẩu", type="password")

    login_btn = st.button("Đăng nhập")

    if login_btn:
        login_animation()
        if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.experimental_rerun()
        else:
            st.error("Sai tên đăng nhập hoặc mật khẩu!")

# Điều hướng
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if st.session_state["logged_in"]:
    main_page(st.session_state["username"])
else:
    login_page()

