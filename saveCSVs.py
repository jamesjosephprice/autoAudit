import os
import shutil

def move_files_with_string(source_folder, dc_string, cmdb_string, destination_folder):
    # Create the destination folder if it doesn't exist
    os.makedirs(destination_folder, exist_ok=True)
    
    # Get the list of files in the source folder
    files = os.listdir(source_folder)
    
    for file in files:
        # Check if the file name contains the specified string
        if dc_string in file:
            # Construct the destination file name
            destination_name = "desktop_central" + os.path.splitext(file)[1]

        if cmdb_string in file:
            # Construct the destination file name
            destination_name = "cmdb" + os.path.splitext(file)[1]
           
        if dc_string in file or cmdb_string in file:
            # Construct the source and destination file paths
            source_path = os.path.join(source_folder, file)
            destination_path = os.path.join(destination_folder, destination_name)
            print(source_folder + source_path)

            # Move the file to the destination folder
            shutil.move(source_path, destination_path)
    
    print("Files moved successfully!")

# Specify the source folder, string to search for, and the destination folder
source_folder = "/Users/japrice/Downloads"
dc_string_to_search = "IA-IT21b"
cmdb_string_to_search = "ci_export"
destination_folder = "/Users/japrice/Downloads/currentAudit"

# Call the function to move the files
move_files_with_string(source_folder, dc_string_to_search, cmdb_string_to_search, destination_folder)
