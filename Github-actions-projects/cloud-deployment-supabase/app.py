import requests
import pandas as pd
import os

# Define the API endpoint
API_URL = 'https://jsonplaceholder.typicode.com/posts'

# Define the data folder
DATA_FOLDER = 'data'
os.makedirs(DATA_FOLDER, exist_ok=True)

# Make the API request
response = requests.get(API_URL)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Assuming the API returns JSON data
    
    # Convert the data to a pandas DataFrame
    df = pd.DataFrame(data)
    
    # Define the CSV file path
    csv_file_path = os.path.join(DATA_FOLDER, 'data.csv')
    
    # Save the DataFrame to a CSV file
    df.to_csv(csv_file_path, index=False)
    
    print(f"Data successfully saved to {csv_file_path}")
else:
    print(f"Failed to fetch data from the API. Status code: {response.status_code}")
