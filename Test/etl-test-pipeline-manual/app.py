import pandas as pd
import requests
import datetime

# Define the log file
log_file = 'etl_log.txt'

def log_message(message):
    with open(log_file, 'a') as f:
        f.write(f'{datetime.datetime.now()} - {message}\n')

try:
    # Extract
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    data = response.json()

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Transform
    df['title_length'] = df['title'].apply(len)
    df['body_length'] = df['body'].apply(len)
    etl_timestamp = datetime.datetime.now()
    df['etl_timestamp'] = etl_timestamp

    # Load
    df.to_csv('transformed_data.csv', index=False)
    log_message(f'ETL job completed at {etl_timestamp} and data saved to transformed_data.csv')

except Exception as e:
    log_message(f'ETL job failed with error: {e}')
