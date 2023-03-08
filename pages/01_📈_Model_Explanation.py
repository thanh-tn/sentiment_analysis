import streamlit as st
import base64

st.set_page_config(page_title="Model Explanation", page_icon="📈")

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

def intro():
    st.markdown("""
    ## **Introduction about Sentiment Analysis and The Model Result**
    ---
    ### I. **Sentiment Analysis** """)
    st.image("files/model_1.png", caption="Sentiment Analysis")

    st.markdown("""
    **Sentiment analysis** is a technique used to analyze the emotions, attitudes, and opinions expressed in textual data. In the case of Shopee customers, sentiment analysis can be used to understand how customers feel about their shopping experience on the platform. By analyzing customer feedback, reviews, and comments, businesses can gain valuable insights into areas where they are performing well and areas where they need to improve.

    There are several benefits to conducting sentiment analysis for **Shopee customers:**

    *   First, it can help businesses to identify common pain points and areas for improvement, allowing them to make targeted changes that improve the overall customer experience. 
    *   Second, sentiment analysis can help businesses to identify trends in customer behavior and preferences, allowing them to tailor their offerings and marketing messages to better meet customer needs.
    *    Finally, sentiment analysis can be used to measure the success of marketing campaigns and other initiatives, allowing businesses to adjust their strategies based on customer feedback.

    Overall, sentiment analysis is a powerful tool for businesses looking to improve their customer experience on Shopee. By analyzing customer feedback and using the insights gained to make targeted improvements, businesses can build stronger relationships with their customers and drive long-term success.
    """)
    st.markdown("""
    
    ### II. **Model Selection**

    Using **LogisticRegression, MultinomialNB, BernoulliNB, DecisionTreeClassifier, RandomForestClassifier** for this project, below is the comparision of those model for this project
    
    """)
    st.image("files/model_2.png", caption="Model comparision")
    col11, col12 = st.columns(2)
    
    with col11:
        st.image("files/model_3.png", caption="Accuracy")
        st.image("files/f_1.png", caption="F1 Score")

    with col12:
        st.image("files/AUC_ROC.png", caption="AUC_ROC")
        st.image("files/Time_fit.png", caption="Time fit")

    st.markdown("""
    *   LogisticRegression (LR) and RandomForestClassifier (RFC) have the best result, however **LR has time fit is much shorter than RFC -> Select LR model for this case**

    ### **III. LogisticRegression Model**

    #### **1\.  LogisticRegression definition**

    """)
    st.image("files/LR.jpg", caption="Logistic Regression")
    st.markdown("""
    **Logistic regression** is a statistical technique used to analyze and model the relationship between a categorical dependent variable and one or more independent variables. It is commonly used in data science and machine learning for binary classification problems, where the goal is to predict whether an observation belongs to one of two classes (e.g., "yes" or "no," "true" or "false," "spam" or "not spam," etc.).

    **In logistic regression**, the dependent variable is binary (i.e., it takes on one of two values), and the independent variables can be either continuous or categorical. The logistic regression model estimates the probability that an observation belongs to a particular class (e.g., the probability that an email is spam), based on the values of the independent variables.

    #### 2\. **Logistic regression resulted in this project**
    """)
    st.image("files/lr_result.png", caption="Classification Report")
    st.image("files/lr_cf.png", caption="Confusion Matrix")
    st.markdown("""
    *   The accuracy is good at `**0.92**`, however the model predicts for class `1` still not good as class `0` even after resample and turning parameter
    
    """)

intro()

