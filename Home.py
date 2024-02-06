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
        
        Integrating ControlNet, M-LSD (Line Segment Detector), YOLO (You Only Look Once), GPT-4 Vision, Stable Diffusion, and Segment Anything, this system offers a comprehensive solution for room decor and interior design. From understanding spatial layouts and object relationships to generating visually appealing decor suggestions, this project represents a significant leap in automated interior design services.

        Components:

        M-LSD Processed Image:

        Initial image processing utilizes M-LSD to enhance the understanding of room structures, identifying key lines and segments that define space, furniture alignment, and architectural details. This structural comprehension is vital for accurate space planning and design element placement.
        YOLO (You Only Look Once):

        YOLO is employed for its robust object detection capabilities, recognizing and categorizing existing decor items, furniture, and other room elements. This information is crucial for inventory management, style consistency checks, and understanding the functional aspects of the space.
        ControlNet:

        Serving as the project's backbone, ControlNet ensures seamless integration of structural data from M-LSD and object insights from YOLO. It maintains the coherence of spatial and object data, enabling precise and context-aware design interventions.
        GPT-4 Vision:

        Leveraging the descriptive power of GPT-4 Vision, the system offers rich, context-aware descriptions and suggestions for room decor. It can suggest thematic designs, offer decor advice, and provide creative and functional insights into optimizing room layouts, color schemes, and furniture arrangements.
        Stable Diffusion:

        Stable Diffusion is utilized for its potent image generation capabilities. Based on the room's current setup and the desired decor style, it can visualize potential design changes, offering users a glimpse of different decor scenarios, wall colors, furniture arrangements, and lighting effects before any physical changes are made.
        Segment Anything:

        "Segment Anything" is crucial for detailed analysis and segmentation of different room elements. It allows the system to understand and manipulate specific aspects of the room decor, such as changing textures, colors, or styles of individual objects, ensuring that each element contributes harmoniously to the overall aesthetic.
        Conclusion:

        The AI-Enhanced Room Decor Assistant is not just a tool but a revolutionary approach to interior design. It marries the precision of AI in understanding spaces and objects with the creative potential of AI in generating visually appealing and contextually relevant decor suggestions. Whether for professional interior designers seeking an advanced tool to streamline their workflow or homeowners looking for an intuitive system to beautify their living space, this project offers an innovative, efficient, and customizable solution, redefining the future of room decor and interior design.
        """
    with cols[1]:
        st_lottie(lottie_healthy, height=300, key="healthy")