import streamlit as st
import qrcode
from io import BytesIO

st.markdown("<h1 style= 'text-align: center'>QR Code Generator</h1>", unsafe_allow_html= True)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:

 sub_col1, sub_col2 = st.columns([4, 1])

 with sub_col1:
  url = st.text_input("", placeholder= "https://www.example.com", label_visibility="collapsed")
 with sub_col2:
  generate_btn = st.button("Go")

 
 if url:
   qr = qrcode.QRCode()
   qr.add_data(url)


   img = qr.make_image()


   buf = BytesIO()
   img.save(buf, format="PNG")
   byte_im = buf.getvalue()

   st.image(byte_im, "Generated Successfully")
