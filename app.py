import streamlit as st
import room_survey  # Import the room_survey module
import image

st.sidebar.title("Navigation")
icon_home = "🏠"
icon_survey = "📋"
icon_image = "🖼️"

# Create a sidebar menu for navigation
selected_page = st.sidebar.radio(
    "Select a Page",
    {
        icon_home + " Main Page": "Main Page",
        icon_survey + " Room Survey": "Room Survey",
        icon_image + " Image Page": "Image Page",
    },
)

if selected_page == "🏠 Main Page":
    # Add content for the main page
    st.title("Welcome to Room Survey App")
    st.write("This is the main page of the app.")
elif selected_page == "📋 Room Survey":
    # Call the survey function from the room_survey module
    room_survey.survey()
elif selected_page == "🖼️ Image Page":
    # Call the function from the image module
    image.display_image()
