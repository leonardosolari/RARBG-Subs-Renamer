# SubsRenamer
# Copyright (C) 2023  Leonardo Solari

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



from models import files, RARBGmovies, RARBGtvshows
import os
from os import name
from termcolor import colored

def clear():
    #for windows 
    if name == 'nt':
        _ = os.system('cls')
    #for mac and linux
    else:
        _ = os.system('clear')

def banner():
    print(colored("""
 _____       _         ______                                     
/  ___|     | |        | ___ \                                    
\ `--. _   _| |__  ___ | |_/ /___ _ __   __ _ _ __ ___   ___ _ __ 
 `--. \ | | | '_ \/ __||    // _ \ '_ \ / _` | '_ ` _ \ / _ \ '__|
/\__/ / |_| | |_) \__ \| |\ \  __/ | | | (_| | | | | | |  __/ |   
\____/ \__,_|_.__/|___/\_| \_\___|_| |_|\__,_|_| |_| |_|\___|_|
    """, "red"))


if __name__ == "__main__":

    clear()
    banner()
    print("What subtitles are we working with?")
    print("(1) - RARBG movie\n(2) - RARBG tv show")
    mode = input("Choose a model: ")
    
    print("Choose the directory containing the movie(s) or the tv show(s)")
    directory = files.askForDirectory()

    clear()
    banner()
    print("Every subtitle file found in " + colored(directory, "green") + " will be renamed and copied according to the choosen model.")

    stop = input("Are you sure? (Y/N) ")
    if (stop.upper() == "N"):
        exit()

    if(stop.upper() == "Y"):
        if (mode == "1"):
            RARBGmovies.run(directory)

        if (mode == "2"):
            RARBGtvshows.run(directory)

