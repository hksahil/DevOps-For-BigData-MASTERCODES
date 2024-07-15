# code.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def main():
    environment = os.getenv("ENVIRONMENT")
    
    print("Environment:", environment)
    
    # Create a simple DataFrame
    data = {
        'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 23, 32, 35],
        'Salary': [50000, 60000, 55000, 70000]
    }
    df = pd.DataFrame(data)
    print("DataFrame:")
    print(df)
    
    # Perform some numerical operations using numpy
    avg_salary = np.mean(df['Salary'])
    print("Average Salary:", avg_salary)
    
    # Plotting a simple bar chart using matplotlib
    plt.bar(df['Name'], df['Salary'])
    plt.xlabel('Name')
    plt.ylabel('Salary')
    plt.title('Salary Distribution')
    plt.show()

if __name__ == "__main__":
    main()
