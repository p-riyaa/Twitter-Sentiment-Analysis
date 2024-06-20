import streamlit as st
st.set_page_config(layout="wide")
st.title("TWITTER SENTIMENT ANALYSIS")
tweet = st.text_input("Enter the Tweet")
if st.button('Predict Polarity'):
    predicts = load_model.predict(preprocessing(post))
    if(predicts==[1]):
        st.success("Positive Tweet")
    else:
        st.failure("NEGATIVE TWEET")
