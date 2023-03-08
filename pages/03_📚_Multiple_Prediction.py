## Import library
import streamlit as st
import pandas as pd
import numpy as np
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import base64

from libs.udf_functions import *  ## load pre-define fuctions


st.set_page_config(page_title="Multiple prediction", page_icon="📚")

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

### Load model
pred_model = load_obj('Shopee_Review_LogisticRegression.pkl')
count_vector = load_obj('Count_tfidf.pkl')

def predict_new(x_new, pred_model=pred_model, count_vector= count_vector):
    x_new = text_preprocessing(x_new)
    x_new= count_vector.transform(np.array([x_new])).toarray()
    y_hat = pred_model.predict(x_new)
    if y_hat == 1:
        return "Like" # (Like 👍)
    else: 
        return "Not like" # (Dislike 👎)

def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv(index=False).encode('utf-8')

def multiple_prediction():
    st.title("Sentiment Analysis for Shopee Customers 🛒")
    st.write("***Bulk prediction***")
    uploaded_file = st.file_uploader("Choose a CSV file for prediction")

    apply_button = st.button("🔎 Predict 'Like 👍' or 'Dislike 👎'")
    if apply_button:
        if uploaded_file is not None:
            try:
                df = pd.read_csv(uploaded_file, encoding="utf-8")
                df["prediction"] = df.apply(lambda x:predict_new(x["text_review"],pred_model=pred_model, count_vector= count_vector), axis=1)
                st.write("Here is the result:")
                st.write(df)
                csv = convert_df(df)
                st.download_button(
                    label="Download data as CSV",
                    data=csv,
                    file_name='Shopee_review_prediction.csv',
                    mime='text/csv',
                )

            except:
                st.warning("🚨Wrong file format, pls using below formar for your work")
                url_template = "https://drive.google.com/file/d/1OUaYqTTadYYD_n0D4KALZRcaomuFm19i/view?usp=share_link"
                st.markdown(f'<a href="{url_template}" rel="noopener noreferrer" target="_blank">Shopee Review Template </a>',unsafe_allow_html=True)
        else:
            st.warning("🚨Missing upload file!")

                
multiple_prediction()
          


