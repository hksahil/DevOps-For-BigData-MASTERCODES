import streamlit as st
import pandas as pd

# Function to create a DataFrame
def create_dataframe():
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [24, 27, 22, 32],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
    }
    df = pd.DataFrame(data)
    return df

# Function to transform the DataFrame
def transform_dataframe(df):
    df['Age Group'] = pd.cut(df['Age'], bins=[0, 25, 30, 35], labels=['<25', '25-30', '>30'])
    return df

# Streamlit app
st.title("DataFrame Creation and Transformation")

st.write("## Original DataFrame")
df = create_dataframe()
st.write(df)

st.write("## Transformed DataFrame")
transformed_df = transform_dataframe(df)
st.write(transformed_df)
