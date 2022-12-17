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
    mode = input("Choose a mode: ")
    
    print("Choose the directory")
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

