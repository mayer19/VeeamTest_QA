import os
import shutil
from time import sleep

src_path = r"/Users/bernardomachado/PycharmProjects/VeeamTest/original"
dest_path = r"/Users/bernardomachado/PycharmProjects/VeeamTest/copy"

def sync_folder (source, destination):
    # source and destination paths
    src_path = source
    dest_path = destination

    # list source and destination files
    original_files = os.listdir(src_path)
    destination_files = os.listdir(dest_path)

    # change directory to source folder
    #os.chdir(src_path)

    # Loop to copy files from the original folder to the destination folder
    for file in original_files:
        source_file_path = os.path.join(src_path, file)
        destination_file_path = os.path.join(dest_path, file)
        #Copy files
        if os.path.isfile(source_file_path):
            shutil.copy(source_file_path, destination_file_path)
        #Copy directories
        if os.path.isdir(source_file_path):
            #check if folder exist in path, delete and copy
            if file in destination_files:
                #First remove old directory
                shutil.rmtree(destination_file_path)
                #Second copy new direcroty
                shutil.copytree(source_file_path, destination_file_path, dirs_exist_ok=True)
            else:
                #Just copy if directory doe not exist
                shutil.copytree(source_file_path, destination_file_path, dirs_exist_ok=True)


    #Delete files on destionation folder if they are not in original folder
    for file in destination_files:
        if file not in original_files:
            if os.path.isdir:
                shutil.rmtree(os.path.join(dest_path, file))
            elif os.path.isfile:
                shutil.rm(destination_file_path)


    print('-------------')
    print("Original folder: ", os.listdir(src_path))
    print("Destination file: ", os.listdir(dest_path))
    if os.listdir(src_path) == os.listdir(dest_path):
        print("Folder syncronized successfully.")
    else:
        print("Folder are NOT syncronized.")


#Run fucntion and sync each 10 secinds
while True:
    sync_folder(src_path, dest_path)
    sleep(10)