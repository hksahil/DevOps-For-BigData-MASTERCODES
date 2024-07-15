import streamlit as st

# Title of the application
st.title('Interactive Data Application')

# Displaying a text message
st.write('Hello, welcome to this enhanced Streamlit app!')

# Text input from the user
user_name = st.text_input('Enter your name:', 'Sahil')

# Number input from the user
number = st.number_input('Enter a number:', min_value=0, max_value=100, value=50)

# Select box input
color = st.selectbox('Choose a color:', ['Red', 'Green', 'Blue'])

# Slider input
slider_value = st.slider('Select a value:', min_value=0, max_value=100, value=25)

# Button to submit the inputs
if st.button('Submit'):
    st.write(f'Hello {user_name}, you entered the number {number} and selected the color {color}. The slider value is {slider_value}.')

# Generate some sample data for the charts using basic Python
data_length = 20
chart_data = {
    'a': [i for i in range(data_length)],
    'b': [i**2 for i in range(data_length)],
    'c': [i**0.5 for i in range(data_length)]
}

# Display the line chart
st.line_chart(chart_data)

# Display the bar chart
st.bar_chart(chart_data)


