import streamlit as st

# Title of the web app
def survey():
    st.title("AI Interior Decorator Survey")

    # Section 0: Welcome Text
    st.write("Welcome to the AI Interior Decorator survey. Help us understand your preferences so we can design the perfect room for you.")

    # Start a form
    with st.form(key='decor_form'):
        # Section 1: Image Selection for Room Theme
        st.header("Room Theme Preference")
        st.write("Select an image that best represents your preferred room theme.")

        # Variables to store user choices
        room_theme = None

        # Display images in a 2x2 grid
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.image("images/pastel.png", caption="Classic")
            pastel = st.checkbox('Pastel', key='1')
        
        with col2:
            st.image("images/tech.png", caption="Modern")
            tech_savy = st.checkbox('Tech and Savy', key='2')
        
        with col3:
            st.image("images/retro_inspired.png", caption="Vintage")
            retro = st.checkbox('Retro', key='3')
        
        with col4:
            st.image("images/modern.png", caption="Minimalist")
            modern = st.checkbox('Modern', key='4')
        
        # Determine room theme based on checkboxes
        if pastel:
            room_theme = "pastel"
        elif tech_savy:
            room_theme = "tech_savy"
        elif retro:
            room_theme = "retro"
        elif modern:
            room_theme = "modern"

        # Section 2: Wall Color
        st.header("What's your favorite color?")
        wall_color = st.selectbox(
            "Select your favorite wall color:", ("White", "Beige", "Gray", "Blue", "Other")
        )

        # Section 3: Furniture Types
        st.header("Furniture Types")
        furniture_types = st.multiselect(
            "Select your favorite furniture types:",
            ["Sofa", "Bed", "Table", "Chair", "Cabinet"],
        )

        # Additional Questions: Add more questions here to understand the user's preferences.
        st.header("Additional Preferences")
        # Example Question: Flooring Preference
        flooring = st.radio(
            "Select your preferred type of flooring:",
            ("Hardwood", "Carpet", "Tiles", "Laminate", "Other")
        )
        
        # Example Question: Natural Light
        natural_light = st.slider(
            "How important is natural light in your space (1: Not Important, 10: Very Important)?", 1, 10, 5
        )

        # Submit button for the form
        submit_button = st.form_submit_button(label='Submit Results')

    if submit_button:
        # Display user's choices
        if room_theme is not None:
            st.success(f"Preferred Room Theme: {room_theme}")
        else:
            st.error("Please select a room theme.")
        
        st.success(f"Favorite Wall Color: {wall_color}")
        st.success(f"Favorite Furniture Types: {', '.join(furniture_types)}")
        st.success(f"Preferred Flooring Type: {flooring}")
        st.success(f"Importance of Natural Light: {natural_light}")
        # ... display other choices
        
if __name__ == "__main__":
    survey()
