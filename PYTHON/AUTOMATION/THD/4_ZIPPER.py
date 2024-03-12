import os
import shutil
import logging

def zip_folders(base_directory, stores):
    zipped_directory = os.path.join(base_directory, 'zipped')
    if not os.path.exists(zipped_directory):
        os.makedirs(zipped_directory)
        logging.info(f"Created 'zipped' directory '{zipped_directory}'")

    for folder_name in os.listdir(base_directory):
        if folder_name.startswith('ST') and folder_name[2:6] in stores:
            folder_path = os.path.join(base_directory, folder_name)
            if os.path.isdir(folder_path):
                zip_file_path = os.path.join(zipped_directory, f'{folder_name}.zip')
                shutil.make_archive(zip_file_path[:-4], 'zip', folder_path)
                logging.info(f"Folder '{folder_name}' zipped to '{zip_file_path}'")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    # Prompting user for directory
    base_directory = input("Enter the directory path: ").strip()

    # Check if the directory exists
    if not os.path.exists(base_directory):
        logging.error(f"The directory '{base_directory}' doesn't exist.")
    else:
        stores = ['7146', '7262', '1855', '3847', '4020', '4742', '6377']
        zip_folders(base_directory, stores)