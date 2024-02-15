import os
import shutil

folder_path = "Data Set/Child Protection"

# to rename each file starting ftom n
start_number = 10000

for i, filename in enumerate(os.listdir(folder_path)):
    # Get the full path of the file
    file_path = os.path.join(folder_path, filename)
    # Construct the new file name replacing the old one with a number n...
    new_file_name = str(start_number + i) + os.path.splitext(filename)[1]
    new_file_path = os.path.join(folder_path, new_file_name)
    # Use the os.rename() function to rename the file
    os.rename(file_path, new_file_path)



folder_name = os.path.basename(folder_path)

for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        # Get the full path of the file
        file_path = os.path.join(folder_path, filename)
        # Construct the new file name joining the folder name to old n
        new_file_name = folder_name + "." + filename
        new_file_path = os.path.join(folder_path, new_file_name)
        # Use the shutil library to rename the file
        shutil.move(file_path, new_file_path)