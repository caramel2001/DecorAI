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
    "https://assets2.lottiefiles.com/packages/lf20_hxart9lz.json"
)
lottie_welcome = load_lottieurl(
    "https://assets6.lottiefiles.com/packages/lf20_ikvz7qhc.json"
)
lottie_healthy = load_lottieurl(
    "https://assets2.lottiefiles.com/packages/lf20_m0ze3ipv.json"
)

st.title("Welcome to EduAI!")
st_lottie(lottie_welcome, height=300, key="welcome")
st.header("Learning made easy")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("##")
        st.write(
            """
            AI-powered summarization tools can help students to quickly understand the key takeaways from lengthy articles, research papers, and other educational materials. These tools can also help educators to quickly scan through a large amount of content and identify the most important information to present to their students. By using AI to summarize educational materials, students can save time and focus on understanding the most important concepts.
            
            Our product is designed to help you summarize notes and videos, and generate questions and answers based on the provided text. It utilizes state-of-the-art AI technology to provide accurate and concise summaries, as well as generate questions and answers that help you better understand and retain information. Whether you're a student looking to prepare for an exam, or a professional looking to stay on top of the latest industry trends, our product can help you save time and improve your learning experience.

            """
        )
        st.write("##")
        st.write(
            "[Learn More >](https://www.unesco.org/en/digital-education/artificial-intelligence"
        )
    with right_column:
        st_lottie(lottie_health, height=500, key="check")

with st.container():
    st.write("---")
    cols = st.columns(2)
    with cols[0]:
        st.header("How it works?")
        """
Our cutting-edge application is designed to revolutionize the way you learn by simplifying the process of summarizing video lectures and handwritten notes. Whether you're a student, professional, or just someone looking to expand your knowledge, our platform is the perfect solution for you.

All you need to do is provide us with the URL of the video or upload the handwritten notes, and our advanced algorithms will process the information to generate a concise summary. Additionally, our platform can also generate question-answer pairs based on the summary, making it easier for you to grasp the key concepts and retain the information.

With our user-friendly interface, you can quickly access the summary and question-answer pairs on any device, making learning convenient and accessible. Say goodbye to the hassle of manually sifting through hours of lecture material or pages of notes. Let our application do the heavy lifting for you, so you can focus on mastering the material and achieving your learning goals. 
    
        """
    with cols[1]:
        st_lottie(lottie_healthy, height=300, key="healthy")