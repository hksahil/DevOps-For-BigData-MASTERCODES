import streamlit as st

# Set the title of the app
st.title("Basic Streamlit App1")

# Add a text input box
user_input = st.text_input("Enter some text:")

# Add a button
if st.button("Display Text"):
    # Display the input text when the button is clicked
    st.write("You entered:", user_input)
