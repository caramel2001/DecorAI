import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


def display_image():

    # Create a title and sub-title
    st.title("Image Upload")

    # File uploader allows user to add their own image
    uploaded_file = st.file_uploader(
        "Upload the picture of your empty room and let us work our magic",
        type=["jpg", "jpeg", "png"],
    )

    if uploaded_file is not None:
        # Open and display the image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Perform any other operations on the image here
        st.write("Image Uploaded Successfully!")


if __name__ == "__main__":
    display_image()
