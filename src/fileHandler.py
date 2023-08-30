
import os
import sys
def get_files():
    foundFiles = []
    script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    directory = script_directory + "\\assets\\readFiles"
    for file in os.listdir(directory):
        foundFiles.append(file)       
    return foundFiles