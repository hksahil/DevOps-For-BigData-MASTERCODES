import pandas as pd

# Step 1: Read data from a CSV 
input_file = 'input_data.csv'
data = pd.read_csv(input_file)

# Display the first few rows of the data
print("Original neww Dsdsdsata:")
print(data.head())

# Step 2: Perform some basic data manipulations
# For example, let's calculate the average of a numeric column and create a new column with the result

# Check if 'numeric_column' exists in the data
if 'numeric_column' in data.columns:
    data['average_value'] = data['numeric_column'].mean()
else:
    print("Column 'numeric_column' not found in the data.")

# Display the modified data
print("Modified Data:")
print(data.head())

# Step 3: Save the manipulated data to a new CSV file
output_file = 'output_data.csv'
data.to_csv(output_file, index=False)

print(f"Modified data saved to {output_file}")
