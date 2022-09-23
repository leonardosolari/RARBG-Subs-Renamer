import files
import os
from os import name
import shutil
import time

def clear():
    #for windows 
    if name == 'nt':
        _ = os.system('cls')
    #for mac and linux
    else:
        _ = os.system('clear')


clear()
print("Choose the directory")
time.sleep(3)
directory = files.askForDirectory()
filelist = files.findFilesFromExtension(directory, 'srt')
renamed_directory = directory + "/renamedSubtitles"
os.mkdir(renamed_directory)
prev = ""
count = 0
for file in filelist:
    parent_directory_name = files.fileNameFromPath((os.path.abspath(os.path.join(file, os.pardir))))
    if prev == parent_directory_name:
        count += 1
    else:
        count = 0
    new_location = renamed_directory + "/" + parent_directory_name + "-" + str(count) + ".srt"
    shutil.copyfile(file, new_location)
    prev = parent_directory_name

clear()
print("Subtitles have been renamed and copied in " + renamed_directory)
