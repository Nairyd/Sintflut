print ("Sintflut\n\nGenesis 7,23 'So vertilgte er alles, was im Ordner war, vom .pdf, .jpg und .word, bis hin zur kleinsten Datei.'\n\n")

import os
import stat
import time
import shutil


def cleanMove(fileName):
    global movecount
    movecount += 1
    before= path + "\\" + fileName
    after= path + "\\4 Wochen\\" + fileName
    shutil.move(before,after)
    print(fileName," moved to ->\n", after)

def cleaningFunction(a,allAtOnce):
    for root, dirs, files in os.walk("."):
        for name in files:
            fileStatObj=os.stat(name)
            accessTime = fileStatObj.st_atime
            print(name)
            print("Last access: ",time.asctime(time.localtime(accessTime)))
            delayTime=time.time()-accessTime
            daysAgo=((delayTime/60)/60)/24
            print("Thats ",int(daysAgo)," days ago.")
            if daysAgo > a :
                if allAtOnce==False:
                    if input("Should we clean this object? \t y/n?\n") == "y":
                        cleanMove(name) #chose target
                elif allAtOnce==True:
                    cleanMove(name)
            print("\n________________________________________\n")

try:
    movecount = 0
    path = str(os.path.dirname(os.path.realpath(__file__)))
    print("Clean here...",path)
    os.chdir(path)
    files = len([name for name in os.listdir('.') if os.path.isfile(name)])
    print(files,"  Files to check.")

    if not os.path.isdir(path + "\\4 Wochen\\"):
        print("Ordner wird erstellt")
        os.mkdir(path + "\\4 Wochen\\")


    if input("Clean all at once? Or step by step? \t all at once = a\n") == "a":
        cleaningFunction(30,True) # all at once
    cleaningFunction(30,False)     # step by step
finally:
    print(movecount, "//", files," Items cleared!")
    input()
