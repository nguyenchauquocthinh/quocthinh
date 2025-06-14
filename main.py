import streamlit as st

st.set_page_config(page_title="Ký hợp đồng thuê trọ", page_icon="🏠", layout="centered")

# CSS nhẹ để làm đẹp giao diện
st.markdown("""
    <style>
    .contract-box {
        background-color: #f9f9f9;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
        font-size: 18px;
    }
    .signature {
        margin-top: 40px;
        display: flex;
        justify-content: space-between;
    }
    .signature div {
        width: 45%;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Tiêu đề
st.markdown("<h1 style='text-align: center; color: #3b5998;'>📄 HỢP ĐỒNG THUÊ TRỌ</h1>", unsafe_allow_html=True)

# Hình ảnh minh họa
st.image("https://i.imgur.com/yXMMHMY.png", caption="Chàng trai ký hợp đồng với khách", use_column_width=True)

# Hộp hợp đồng
with st.container():
    st.markdown("<div class='contract-box'>", unsafe_allow_html=True)
    st.markdown("### BÊN CHO THUÊ (BÊN A):")
    st.text("Họ và tên: Nguyễn Văn Thịnh\nSố điện thoại: 0909 xxx xxx\nĐịa chỉ: 34/4C Ấp Đông Thới, Hóc Môn, TP.HCM")

    st.markdown("### BÊN THUÊ (BÊN B):")
    st.text("Họ và tên: ______________________\nSố điện thoại: _______________\nCMND/CCCD: _______________")

    st.markdown("### THÔNG TIN PHÒNG:")
    st.text("Địa chỉ phòng: 12/3 Đường ABC, Quận XYZ\nGiá thuê: 2.500.000 VNĐ/tháng\nTiền cọc: 1 tháng\nThời gian thuê: 6 tháng")

    st.markdown("### ĐIỀU KHOẢN:")
    st.markdown("- Bên B phải thanh toán đúng hạn hàng tháng.\n- Không được tự ý sửa chữa, thay đổi cấu trúc phòng.\n- Nếu trả phòng trước hạn phải báo trước 30 ngày.")

    st.markdown("</div>", unsafe_allow_html=True)

# Ký tên
st.markdown("""
<div class='signature'>
  <div>
    <strong>BÊN A</strong><br/>
    (Chủ trọ)<br/><br/><br/>
    Nguyễn Văn Thịnh
  </div>
  <div>
    <strong>BÊN B</strong><br/>
    (Người thuê)<br/><br/><br/>
    Ký tên
  </div>
</div>
""", unsafe_allow_html=True)

# Nút xác nhận
if st.button("✅ Xác nhận ký hợp đồng"):
    st.success("🎉 Hợp đồng đã được ký thành công!")





