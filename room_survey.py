import streamlit as st


# Title of the web app
def survey():
    st.title("Room Survey")

    # Section 1: Room Theme
    st.header("Room Theme")
    room_theme = st.radio(
        "Choose a room theme:", ("Classic", "Modern", "Vintage", "Minimalist")
    )

    # Section 2: Wall Color
    st.header("Wall Color")
    wall_color = st.selectbox(
        "Select your favorite wall color:", ("White", "Beige", "Gray", "Blue", "Other")
    )

    # Section 3: Furniture Types
    st.header("Furniture Types")
    furniture_types = st.multiselect(
        "Select your favorite furniture types:",
        ["Sofa", "Bed", "Table", "Chair", "Cabinet"],
    )

    # Submit button
    if st.button("Submit"):
        # Display user's choices
        st.success(f"Room Theme: {room_theme}")
        st.success(f"Favorite Wall Color: {wall_color}")
        st.success(f"Favorite Furniture Types: {', '.join(furniture_types)}")


if __name__ == "__main__":
    survey()
