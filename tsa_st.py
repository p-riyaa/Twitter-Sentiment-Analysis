import streamlit as st
import re
from nltk.corpus import stopwords

st.set_page_config(layout="wide")
st.title("TWITTER SENTIMENT ANALYSIS")

gradient_background = """
<style>
.stApp {
    background: linear-gradient(to right, #FCF97D, #FD8DD4);
    background-attachment: fixed;
}
</style>
"""

# Inject the CSS into the Streamlit app
st.markdown(gradient_background, unsafe_allow_html=True)

import pickle
#loading the trained model
with open('trained_model.pkl','rb') as f:
    load_model = pickle.load(f)

#loading the fitted vectorizer and defining function for preprocessing 
with open('vector.pkl','rb') as f:
    vectorizer = pickle.load(f)

from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
def stemming(content):
  stemmed_content = re.sub('[^a-zA-Z]',' ',content)
  stemmed_content = stemmed_content.lower()
  stemmed_content = stemmed_content.split()
  stemmed_content = [stemmer.stem(word) for word in stemmed_content if not word in stopwords.words('english')]
  stemmed_content = ' '.join(stemmed_content)
  return stemmed_content

def preprocessing(twitter_post):
    stemmed_post =stemming(twitter_post)
    vectorized_X = vectorizer.transform([stemmed_post])
    return vectorized_X

tweet = st.text_input("Enter the Tweet")
if st.button('Predict Polarity'):
    predicts = load_model.predict(preprocessing(tweet))
    if(predicts==[1]):
        st.success("POSITIVE TWEET")
    else:
        st.error("NEGATIVE TWEET")