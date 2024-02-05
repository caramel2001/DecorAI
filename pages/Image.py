import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from backend.generation import run_replicate, controlled_generation


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


def empty_room():
    st.subheader("Add furniture to Empty Room")
    pass


def replace_all():
    st.subheader("Replace All Exisitng Furniture")
    pass


def replace_particular():
    st.subheader("Replace a Particular Furniture")
    pass


def main():
    st.title("AI Interior Decorator")
    # select box
    option = st.sidebar.selectbox(
        "How would you like to generate",
        [
            "Add furniture to Empty Room",
            "Replace All Exisitng Furniture",
            "Replace a Particular Furniture",
        ],
    )
    if option == "Add furniture to Empty Room":
        empty_room()
    elif option == "Replace All Exisitng Furniture":
        replace_all()
    elif option == "Replace a Particular Furniture":
        replace_particular()


if __name__ == "__main__":

    main()
