# Author:      brandan
# Created:     28/08/2013
#-------------------------------------------------------------------------------
this_file = "Directory.py"
title = "Brandans Directory Lister!"

import os
def main():
    files_in_dir = os.listdir(os.curdir)
    count = 0
    for file_in_dir in files_in_dir:
        count = count + 1
    print(title)
    print(str(count) + " items")
	
    #save = raw_input("Save the dir out? (y/n)")
    save = "y"
    prefix = raw_input("Prefix: ")
    suffix = raw_input("Suffix: ")
	
    if save.lower() == "y":
        file = open("log.txt", "w")
        file.write(title + "\n")
        file.write("(excluding: " + this_file + ")\n\n")
        for file_in_dir in files_in_dir:
            if file_in_dir != this_file:
                file.write(prefix + file_in_dir + suffix + '\n')

if __name__ == '__main__':
    main()
