# code.py
import pandas as pd
import os

def main():
    environment = os.getenv("ENVIRONMENT")
    
    print("Environment:", environment)
    
    data = {
        'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 23, 32, 35]
    }
    df = pd.DataFrame(data)
    print("DataFrame:")
    print(df)

if __name__ == "__main__":
    main()
