import os
import sys
def get_asset_path():
    script_directory = os.path.dirname(os.path.abspath(sys.argv[0]))
    return script_directory + "\\assets\\"

def get_files():
    foundFiles = []
    directory = get_asset_path + "\\readFiles"
    for file in os.listdir(directory):
        foundFiles.append(file)       
    return foundFiles