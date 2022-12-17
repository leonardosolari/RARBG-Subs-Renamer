from models import files
import shutil

def run(directory):
    filelist = files.findFilesFromExtension(directory, 'srt')
    prev = ""
    count = 0
    substring = "english"
    for file in filelist:
        if (substring not in file.lower()):
            continue
        splitted = file.split("/")
        parent_directory_name = splitted[len(splitted) - 3]
        if (prev == parent_directory_name):
            count += 1
        else:
            count = 0
        
        if (directory.endswith(parent_directory_name)):
            new_location = directory + "/" + parent_directory_name + "-" + str(count) + ".srt"
        else:
            new_location = directory + "/" + parent_directory_name + "/" + parent_directory_name + "-" + str(count) + ".srt"
        shutil.copyfile(file, new_location)
        prev = parent_directory_name
    print("")
    print("Subtitles have been renamed with success")

