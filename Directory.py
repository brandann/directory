# Author:      brandan
# Created:     28/08/2013
#-------------------------------------------------------------------------------

import os
def main():
    files_in_dir = os.listdir(os.curdir)
    print "mb\tgb\tName"
    print "(int)\t(int)"
    print "-------------------------------------------------------"
    for file_in_dir in files_in_dir:
        mb = (os.path.getsize(file_in_dir)/1024)/1024
        gb = ((os.path.getsize(file_in_dir)/1024)/1024)/1024
        
        print mb, "\t", gb, "\t", file_in_dir
    #save = raw_input("Save the dir out? (y/n)")
    save = "y"
    if save.lower() == "y":
        file = open("log.txt", "w")
        file.write("Brandans File Directory Manager!\n\n")
        for file_in_dir in files_in_dir:
            file.write(file_in_dir + '\n')

if __name__ == '__main__':
    main()
