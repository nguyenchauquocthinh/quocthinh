import streamlit as st

st.set_page_config(page_title="Ký hợp đồng thuê trọ", page_icon="🏠", layout="centered")

# CSS giao diện (bọc trong <style> đúng chuẩn)
st.markdown("""
    <style>
    .contract-box {
        background-color: #f9f9f9;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
        font-size: 18px;
        margin-top: 20px;
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

# Ảnh minh họa (chàng trai ký hợp đồng)
st.image("https://i.imgur.com/yXMMHMY.png", caption="Chàng trai ký hợp đồng với khách", use_column_width=True)

# Hộp nội dung hợp đồng
st.markdown("<div class='contract-box'>", unsafe_allow_html=True)

st.markdown("### BÊN CHO THUÊ (BÊN A):")
st.text("Họ và tên: Nguyễn Văn Thịnh\nSĐT: 0909 xxx xxx\nĐịa chỉ: 34/4C Ấp Đông Thới, Hóc Môn")

st.markdown("### BÊN THUÊ (BÊN B):")
ten = st.text_input("Họ tên người thuê")
sdt = st.text_input("Số điện thoại người thuê")
cccd = st.text_input("Số CCCD/CMND")

st.markdown("### THÔNG TIN PHÒNG:")
st.text("Địa chỉ phòng: 12/3 Đường ABC, Quận XYZ\nGiá thuê: 2.500.000 VNĐ/tháng\nTiền cọc: 1 tháng\nThời gian thuê: 6 tháng")

st.markdown("### ĐIỀU KHOẢN:")
st.markdown("- Thanh toán đúng hạn mỗi tháng.\n- Không tự ý sửa chữa phòng.\n- Trả phòng sớm cần báo trước 30 ngày.")

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
    {ten}
  </div>
</div>
""".format(ten=ten if ten else "Ký tên"), unsafe_allow_html=True)

# Nút xác nhận
if st.button("✅ Xác nhận ký hợp đồng"):
    if ten and sdt and cccd:
        st.success(f"🎉 Hợp đồng đã được ký thành công với {ten}!")
    else:
        st.warning("⚠️ Vui lòng nhập đầy đủ thông tin người thuê trước khi ký.")






