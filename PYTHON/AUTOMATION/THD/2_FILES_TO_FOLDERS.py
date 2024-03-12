import os
import shutil

# Ask the user for the directory path
directory = input("Enter the directory path: ").strip()

# Check if the directory exists
if not os.path.exists(directory):
    print("Directory does not exist.")
    exit()

# Define the list of store numbers
stores = ['7146', '7262', '1855', '3847', '4020', '4742', '6377']

# Create folders for each store number
for store in stores:
    folder_name = f"ST{store} migration deliverables"
    folder_path = os.path.join(directory, folder_name)
    os.makedirs(folder_path, exist_ok=True)

# Move files to their respective folders
for filename in os.listdir(directory):
    source_path = os.path.join(directory, filename)
    if os.path.isfile(source_path):  # Check if it's a file
        for store in stores:
            if filename.startswith(f"ST{store}"):
                destination_path = os.path.join(directory, f"ST{store} migration deliverables", filename)
                shutil.move(source_path, destination_path)

print("Files moved successfully.")