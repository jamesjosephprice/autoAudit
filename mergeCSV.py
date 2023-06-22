import csv
import os

def merge_csv_columns(desktop_central_file_path, cmdb_file_path, output_path):
    # Extract the file names from the paths
    desktop_central_filename = os.path.splitext(os.path.basename(desktop_central_file_path))[0]
    cmdb_filename = os.path.splitext(os.path.basename(cmdb_file_path))[0]
    
    # Read the first column of CSV1
    csv1_column = []
    with open(desktop_central_file_path, 'r') as csv1_file:
        csv1_reader = csv.reader(csv1_file)
        csv1_title = next(csv1_reader)[0]  # Get the title from the heading row
        for row in csv1_reader:
            csv1_column.append(row[0])
    
    # Read the first column of CSV2
    csv2_column = []
    with open(cmdb_file_path, 'r') as csv2_file:
        csv2_reader = csv.reader(csv2_file)
        csv2_title = next(csv2_reader)[0]  # Get the title from the heading row
        for row in csv2_reader:
            csv2_column.append(row[0])
    
    # Merge the columns into a new CSV file
    with open(output_path, 'w', newline='') as output_file:
        csv_writer = csv.writer(output_file)
        
        # Write the heading row with the file names as titles
        csv_writer.writerow([desktop_central_filename, cmdb_filename])
        
        # Write the merged columns
        for i in range(max(len(csv1_column), len(csv2_column))):
            csv_writer.writerow([csv1_column[i] if i < len(csv1_column) else '',
                                 csv2_column[i] if i < len(csv2_column) else ''])

# Specify the paths of the two input CSV files and the output CSV file
cmdb_file_path = '/Users/japrice/Downloads/currentAudit/cmdb.csv'
desktop_central_file_path = '/Users/japrice/Downloads/currentAudit/desktop_central.csv'
output_path = '/Users/japrice/Downloads/currentAudit/merged.csv'

# Call the function to merge the columns
merge_csv_columns(desktop_central_file_path, cmdb_file_path, output_path)
