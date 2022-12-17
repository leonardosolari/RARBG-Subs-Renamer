from models import files
import os
import shutil
from termcolor import colored

def run(directory):
    filelist = files.findFilesFromExtension(directory, 'srt')
    renamed_directory = directory + "/renamedSubtitles"
    os.mkdir(renamed_directory)
    prev = ""
    count = 0
    substring = "english"
    for file in filelist:
        if (substring not in file.lower()):
            continue
        parent_directory_name = files.fileNameFromPath((os.path.abspath(os.path.join(file, os.pardir))))
        if prev == parent_directory_name:
            count += 1
        else:
            count = 0
        new_location = renamed_directory + "/" + parent_directory_name + "-" + str(count) + ".srt"
        shutil.copyfile(file, new_location)
        prev = parent_directory_name

    print("")
    print("Subtitles have been renamed and copied in " + colored(renamed_directory, "green"))