#! /usr/bin/env python
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      brandan
#
# Created:     28/08/2013
# Copyright:   (c) brandan 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import os, Blogo13
def main():
    files_in_dir = os.listdir(os.curdir)
    print "mb\tgb\tName"
    print "(int)\t(int)"
    print "-------------------------------------------------------"
    for file_in_dir in files_in_dir:
        mb = (os.path.getsize(file_in_dir)/1024)/1024
        gb = ((os.path.getsize(file_in_dir)/1024)/1024)/1024
        
        print mb, "\t", gb, "\t", file_in_dir
    save = raw_input("Save the dir out? (y/n)")
    if save.lower() == "y":
        file = open("log.txt", "w")
        file.write("Brandans File Directory Manager!\n\n")
        for file_in_dir in files_in_dir:
            if os.path.getsize(file_in_dir) > 1:
                file.write(file_in_dir + '\n')

if __name__ == '__main__':
    Blogo13.run()
    main()
