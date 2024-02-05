import requests
import streamlit as st
from streamlit_lottie import st_lottie
import time
import streamlit as st
import boto3
import json
import os
import uuid


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_health = load_lottieurl(
    "https://lottie.host/01f57564-e121-4554-be96-1de0e1d50990/4NRuwVVJBs.json"
)
lottie_welcome = load_lottieurl(
    "https://lottie.host/77be6c69-cc89-4fa8-9e80-e31462ec9fcb/nHLA4yoRzv.json"
)
lottie_healthy = load_lottieurl(
    "https://lottie.host/2cb5041e-96ab-4ba5-957a-1630808c21b3/vwixiYWwjj.json"
)

st.title("Welcome to DecorAI!")
st_lottie(lottie_welcome, height=300, key="welcome")
st.header("Dreams Home made easy")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("##")
        st.write(
            """
           Welcome to DecorAI, where the future of room decoration is made simple and intuitive through the power of Artificial Intelligence. Our platform is dedicated to transforming your living spaces into stunning interiors with the assistance of advanced AI technology.

At DecorAI, we believe that everyone deserves a beautiful home. Our AI-powered tools are designed to understand your unique style and space, offering personalized design solutions that fit your life
            """
        )
        st.write("##")
        
    with right_column:
        st_lottie(lottie_health, height=300, key="check")

with st.container():
    st.write("---")
    cols = st.columns(2)
    with cols[0]:
        st.header("How it works?")
        """
        Smart AI Designer: Just upload pictures of your room and our AI will analyze the space, lighting, and existing furniture to provide tailored design recommendations. Whether you're revamping a cozy bedroom or a spacious living room, our AI understands your needs.
        
        Personalized Style Assessment: Not sure of your style? Our AI will guide you! Complete our interactive quiz, and the AI will suggest decor themes that resonate with your taste, from modern minimalist to bohemian chic    
        """
    with cols[1]:
        st_lottie(lottie_healthy, height=300, key="healthy")