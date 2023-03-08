#### ===================================================|
#### Project 1: Sentiment_Analysis (Predict Model ML)   |
#### Name: Trần Ngọc Thành                              |
#### Email: thanhtn.tnt@gmail.com                       |
#### ===================================================|

import streamlit as st
import base64

# set page layout
st.set_page_config(
    page_title="Sentiment Analysis for Shopee Customers",
    page_icon="👋",
    # layout="wide",
    initial_sidebar_state="expanded",
)

# Set background image
def background_image(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

image_file = 'files/bg_1.jpg'
background_image(image_file)



st.title("Welcome to the Sentiment Analysis app for Shopee Customers 🛒")

st.image("files/img_1.png")