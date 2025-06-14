import streamlit as st

st.set_page_config(page_title="Ký hợp đồng thuê trọ", page_icon="🏠", layout="centered")

# CSS giao diện
st.markdown("""
    <style>
    .contract-box {
        background-color: #fff;
        padding: 35px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        font-size: 18px;
        margin-top: 20px;
        line-height: 1.8;
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
    .section-title {
        font-weight: bold;
        color: #2c3e50;
        margin-top: 20px;
    }
    ul {
        padding-left: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Tiêu đề
st.markdown("""
<h1 style='text-align: center; color: #2c3e50;'>📄 HỢP ĐỒNG THUÊ PHÒNG TRỌ</h1>
<h4 style='text-align: center; color: #7f8c8d;'>Cam kết giữa bên cho thuê và bên thuê về việc thuê phòng trọ</h4>
""", unsafe_allow_html=True)

# Ảnh minh họa hoạt hình
st.image(
    "https://cdn-icons-png.flaticon.com/512/4139/4139981.png",
    caption="Ký hợp đồng hoạt hình 😄",
    use_container_width=True
)

# Form nhập thông tin
with st.form("contract_form"):
    st.subheader("Thông tin bên thuê (Bên B)")
    ten = st.text_input("Họ tên người thuê", key="ten")
    sdt = st.text_input("Số điện thoại người thuê", key="sdt")
    cccd = st.text_input("Số CCCD/CMND", key="cccd")
    diachi_b = st.text_input("Địa chỉ thường trú của bên B", key="dc_b")
    submit = st.form_submit_button("✅ Xác nhận ký hợp đồng")

# Nội dung hợp đồng chi tiết
contract_html = f"""
<div class='contract-box'>
  <div class='section-title'>BÊN CHO THUÊ (BÊN A):</div>
  <p>
    Họ và tên: Nguyễn Châu Quốc Thịnh<br/>
    SĐT: 0353041765<br/>
    Địa chỉ: 34/4C Ấp Đông Thới, Hóc Môn
  </p>

  <div class='section-title'>BÊN THUÊ (BÊN B):</div>
  <p>
    Họ tên: <strong>{ten if ten else "_______________"}</strong><br/>
    SĐT: <strong>{sdt if sdt else "_______________"}</strong><br/>
    CCCD/CMND: <strong>{cccd if cccd else "_______________"}</strong><br/>
    Địa chỉ thường trú: <strong>{diachi_b if diachi_b else "_______________"}</strong>
  </p>

  <div class='section-title'>THÔNG TIN PHÒNG:</div>
  <p>
    Địa chỉ phòng: 55 Nguyễn Thị Tràng, Quận 12<br/>
    Diện tích: 20m<sup>2</sup><br/>
    Trang bị: Quạt, đèn, nhà vệ sinh riêng, wifi<br/>
    Giá thuê: <strong>2.500.000 VNĐ/tháng</strong><br/>
    Tiền cọc: <strong>2.500.000 VNĐ</strong><br/>
    Hình thức thanh toán: Chuyển khoản hoặc tiền mặt<br/>
    Thời gian thuê: <strong>6 tháng</strong> (có thể gia hạn theo thoả thuận)
  </p>

  <div class='section-title'>ĐIỀU KHOẢN:</div>
  <ul>
    <li>Bên B phải thanh toán tiền thuê đúng hạn trước ngày 05 hàng tháng.</li>
    <li>Không tự ý sửa chữa, thay đổi cấu trúc phòng khi chưa được sự đồng ý của Bên A.</li>
    <li>Không sử dụng phòng vào mục đích trái pháp luật hoặc gây mất an ninh trật tự.</li>
    <li>Nếu Bên B muốn trả phòng sớm, phải báo trước ít nhất 30 ngày.</li>
    <li>Tiền cọc sẽ được hoàn trả nếu không vi phạm các điều khoản hợp đồng.</li>
  </ul>

  <div class='section-title'>HIỆU LỰC HỢP ĐỒNG:</div>
  <p>
    Hợp đồng này có hiệu lực từ ngày ký và được lập thành 02 bản, mỗi bên giữ 01 bản có giá trị pháp lý như nhau.
  </p>
</div>
"""

# Hiển thị hợp đồng
st.markdown(contract_html, unsafe_allow_html=True)

# Chữ ký
st.markdown(f"""
<div class='signature'>
  <div>
    <strong>BÊN A</strong><br/>
    (Chủ trọ)<br/><br/><br/><br/>
    Nguyễn Châu Quốc Thịnh
  </div>
  <div>
    <strong>BÊN B</strong><br/>
    (Người thuê)<br/><br/><br/><br/>
    {ten if ten else 'Ký tên'}
  </div>
</div>
""", unsafe_allow_html=True)

# Kết quả
if submit:
    if ten and sdt and cccd:
        st.success(f"🎉 Hợp đồng đã được ký thành công với {ten}! Bản sao hợp đồng có thể được in hoặc lưu trữ.")
    else:
        st.warning("⚠️ Vui lòng nhập đầy đủ thông tin người thuê trước khi ký.")
