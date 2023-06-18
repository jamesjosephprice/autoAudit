import csv

def find_unique_values(csv_file):
    unique_values = {}
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            col1_val = row[0]
            col2_val = row[1]
            
            if col1_val not in unique_values:
                unique_values[col1_val] = 'Column 1'
            else:
                unique_values.pop(col1_val, None)
            
            if col2_val not in unique_values:
                unique_values[col2_val] = 'Column 2'
            else:
                unique_values.pop(col2_val, None)
    
    return unique_values

# Specify the path to your CSV file
csv_file = 'data.csv'

# Call the function and get the unique values
unique_values = find_unique_values(csv_file)

# Print the unique values and their corresponding columns
for value, column in unique_values.items():
    print(f"Unique value: {value}, Column: {column}")
