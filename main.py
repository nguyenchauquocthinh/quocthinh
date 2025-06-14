import streamlit as st

st.set_page_config(page_title="Ký hợp đồng thuê trọ", page_icon="🏠", layout="centered")

# CSS giao diện
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

# Ảnh minh họa phong cách hoạt hình
st.image("https://i.imgur.com/1qVtIvu.png", caption="Hoạt hình: Ký hợp đồng thuê trọ", use_column_width=True)

# Form nhập thông tin
with st.form("contract_form"):
    ten = st.text_input("Họ tên người thuê", key="ten")
    sdt = st.text_input("Số điện thoại người thuê", key="sdt")
    cccd = st.text_input("Số CCCD/CMND", key="cccd")
    submit = st.form_submit_button("✅ Xác nhận ký hợp đồng")

# Hộp nội dung hợp đồng
contract_html = f"""
<div class='contract-box'>
  <h3>BÊN CHO THUÊ (BÊN A):</h3>
  <p>Họ và tên: Nguyễn Văn Thịnh<br/>
  SĐT: 0909 xxx xxx<br/>
  Địa chỉ: 34/4C Ấp Đông Thới, Hóc Môn</p>

  <h3>BÊN THUÊ (BÊN B):</h3>
  <p>
    Họ tên: <strong>{ten if ten else "_______________"}</strong><br/>
    SĐT: <strong>{sdt if sdt else "_______________"}</strong><br/>
    CCCD/CMND: <strong>{cccd if cccd else "_______________"}</strong>
  </p>

  <h3>THÔNG TIN PHÒNG:</h3>
  <p>Địa chỉ phòng: 12/3 Đường ABC, Quận XYZ<br/>
  Giá thuê: 2.500.000 VNĐ/tháng<br/>
  Tiền cọc: 1 tháng<br/>
  Thời gian thuê: 6 tháng</p>

  <h3>ĐIỀU KHOẢN:</h3>
  <ul>
    <li>Thanh toán đúng hạn mỗi tháng.</li>
    <li>Không tự ý sửa chữa phòng.</li>
    <li>Trả phòng sớm cần báo trước 30 ngày.</li>
  </ul>
</div>
"""

# Hiển thị hợp đồng
st.markdown(contract_html, unsafe_allow_html=True)

# Ký tên
st.markdown(f"""
<div class='signature'>
  <div>
    <strong>BÊN A</strong><br/>
    (Chủ trọ)<br/><br/><br/>
    Nguyễn Văn Thịnh
  </div>
  <div>
    <strong>BÊN B</strong><br/>
    (Người thuê)<br/><br/><br/>
    {ten if ten else 'Ký tên'}
  </div>
</div>
""", unsafe_allow_html=True)

# Kết quả
if submit:
    if ten and sdt and cccd:
        st.success(f"🎉 Hợp đồng đã được ký thành công với {ten}!")
    else:
        st.warning("⚠️ Vui lòng nhập đầy đủ thông tin người thuê trước khi ký.")

