import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import json
from backend.generation import run_replicate, controlled_generation
from recommendation import get_recommendations

def display_image():
    user_pref = None
    # Check if user has submitted his preferences by checking if survey_result.json exists
    try:
        with open("survey_results.json", "r") as file:
            user_pref = json.load(file)
    except FileNotFoundError:
        st.error("Please fill the survey first")
        return None, None  # Return None if survey not filled or file not found
        
    if user_pref:
        st.title("Image Upload")
        uploaded_file = st.file_uploader("Upload the picture of your empty room and let us work our magic", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            return image, user_pref
    return None, None  # Return None if no file is uploaded or user_pref is empty

def empty_room():
    st.subheader("Add furniture to Empty Room")
    # Implement functionality specific to empty rooms here
    pass

def replace_all():
    st.subheader("Replace All Existing Furniture")
    # Implement functionality specific to replacing all furniture here
    pass

def replace_particular():
    st.subheader("Replace a Particular Furniture")
    # Implement functionality specific to replacing particular furniture here
    pass

def main():
    if 'prompt' not in st.session_state:
        st.session_state.prompt = None

    if 'image' not in st.session_state:
        st.session_state.image = None

    if 'output_image' not in st.session_state:
        st.session_state.output_image = None
    st.title("AI Interior Decorator")
    option = st.sidebar.selectbox(
        "How would you like to generate",
        [
            "Add furniture to Empty Room",
            "Replace All Existing Furniture",
            "Replace a Particular Furniture",
        ],
    )
    if option == "Add furniture to Empty Room":
        empty_room()
    elif option == "Replace All Existing Furniture":
        replace_all()
    elif option == "Replace a Particular Furniture":
        replace_particular()
    
    image, user_pref = display_image()

    if image and user_pref:
        print('type', type(image))

        # Only generate the prompt if it hasn't been generated yet
        if not st.session_state.prompt:
            st.session_state.prompt = get_recommendations(image, user_pref)
        
        st.text_area("Prompt", st.session_state.prompt)
        btn = st.button("Finalized Prompt Generate output")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.image(image, caption="INPUT", use_column_width=True)
        
        with col2:
            if not btn:
                st.write("start generating")
            else:           
                with st.spinner('Generating the output...'):
                    # Only generate the output image if it hasn't been generated yet
                    if not st.session_state.output_image:
                        st.session_state.output_image = controlled_generation(image, prompt=st.session_state.prompt)
                    
                    if st.session_state.output_image:
                        st.image(st.session_state.output_image, caption="OUTPUT", use_column_width=True)
                    else:
                        st.error("Failed to generate the output image.")
                st.write("Done!")


if __name__ == "__main__":
    main()
