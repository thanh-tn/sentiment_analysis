
## Import library

import streamlit as st
import numpy as np
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import base64

from libs.udf_functions import *  ## load pre-define fuctions

st.set_page_config(page_title="Single prediction", page_icon="🔍")

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
        return 1 # (Like 👍)
    else: 
        return 0 # (Dislike 👎)


def single_predict():
    # background_image('tiki_background.jpg') 
    
    st.title("Sentiment Analysis for Shopee Customers 🛒")
    x_new = st.text_area("**Please input review:**")
    apply_button = st.button("🔎 Predict 'Like 👍' or 'Dislike 👎'")

    
    if apply_button:
        if x_new == "":
            st.warning("Opp!!!! Missing text... Pls input 🆘🆘🆘")
        else:
            result = predict_new(x_new)
            st.write("***The prediction result is:***")
            # st.write(f"'***{x_new}***'")
            if result == 1:
                # st.write("Like 👍")
                st.image("files/like.png", caption="Like")
            else:
                # st.write("Dislike 👎")
                st.image("files/dislike.png", caption="Dislike")

single_predict()
