import os
import shutil

print("\n")
print("**************************************")
print("*           FILES 2 FOLDERS          *")
print("*         Made by Yashwanth K        *")
print("**************************************")
print("\n")
def move_files_to_directory(source_dir):

    for filename in os.listdir(source_dir):
        if filename.startswith("ST") and len(filename) >= 9 and filename[2:6].isdigit():

            store_number = filename[:6]

            target_dir = os.path.join(source_dir, f"{store_number} migration deliverables")

            if not os.path.exists(target_dir):
                os.makedirs(target_dir)

            shutil.move(os.path.join(source_dir, filename), target_dir)
            print(f"Moved '{filename}' to '{target_dir}'")

source_directory = input("Enter the source directory path: ").strip()

if os.path.isdir(source_directory):
    move_files_to_directory(source_directory)
    print("File migration completed.")
else:
    print("Invalid directory path.")

print("Press Enter to exit...")
input()