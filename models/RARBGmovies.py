# SubsRenamer
# Copyright (C) 2022  Leonardo Solari

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from models import files
import shutil

def run(directory):
    filelist = files.findFilesFromExtension(directory, 'srt')
    prev = ""
    count = 0
    substrings = ["english", "eng", "italian", "ita"]
    for substring in substrings:
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
                new_location = directory + "/" + parent_directory_name + "-" + str(count) + "-" + substring + ".srt"
            else:
                new_location = directory + "/" + parent_directory_name + "/" + parent_directory_name + "-" + str(count) + "-" + substring + ".srt"
            shutil.copyfile(file, new_location)
            prev = parent_directory_name
    print("")
    print("Subtitles have been renamed with success")

