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