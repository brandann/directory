#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      brandan
#
# Created:     18/09/2013
# Copyright:   (c) brandan 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import shutil, os

def main():

    #files isnt working
    print "Sorry, but this program isnt working."
    print "The program does not accuratly sort the files resulting in a mixed outcome..."
    OK = raw_input()
    return

    #Set up vars
    inc = 1
    inc_bool = False
    files_in_dir = os.listdir(os.curdir)

    files_in_dir.sort()

    #get file name information
    prefix = raw_input("Prefix: ")
    suffix = raw_input("Suffix: ")
    extension = raw_input("Extension: ")

    #correct extension format
    if '.' not in extension:
        extension = '.' + extension

    #ask where program should start counting
    #assumes correct int value, sets to 1 if not
    incstr = raw_input("Starting integer value: ")
    try:
        inc = int(incstr)
    except Exception:
        inc = 1
        pass

    #main loop
    for file_name in files_in_dir:
        if extension in file_name:
            name = prefix + str(inc) + suffix + extension
            inc += 1
            try:
                shutil.copyfile(file_name, name)
                os.remove(file_name)
                print file_name + " --> "+ name
            except Exception:
                print Exception

if __name__ == '__main__':
    main()
