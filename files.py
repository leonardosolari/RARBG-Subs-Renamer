#COLLECTION OF USEFUL FUNCTIONS TO MANAGE FILES IN PYTHON

from tkinter import Tk, filedialog
import glob
import os

#This procedure asks the user to chose a directory through a dialog window and returns
#a string containing the path of the chosen directory
#Output: string representing path of chosen directory
def askForDirectory():
    root = Tk() #pointing root to Tk() to use it as Tk() in program
    root.withdraw() #hides small tkinter window
    root.attributes('-topmost', True) # Opened windows will be active. above all windows despite of selection
    directory_path = filedialog.askdirectory() #returns opened path as str
    return directory_path



#Input: string representing directory path, string representing a file extension
#Output: string List containing the paths of all the files having ext for extension found in directory_path 
def findFilesFromExtension(directory_path, ext):
    fileList = glob.glob(directory_path + "/**/*." + ext, recursive = True)
    return fileList

#Input: string = complete path of a file. Eg: "/Users/user/file.ext"
#Output: string = file name. Eg: "file.ext"
def fileNameFromPath(file_path):
    file_name = os.path.basename(os.path.normpath(file_path))
    return file_name





