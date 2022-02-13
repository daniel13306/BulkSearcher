import time as t
import keyboard as kb
import pathlib
from os import walk
from os import system
system("title " + 'BulkSearcher by DeadEagle [www.Coding-Community.com]')

# Source code by DeadEagle
# https://www.coding-community.com

# Variables
filelist,foundlist,filecount,hitcount,Searchword,filetype,folder = [],[],0,0,input("Enter your Keyword: "),input("Enter the filetype you want to search through: "),input("Specify your folder (press enter to check in THIS folder): ")
print("\n")

def IterateFiles(filelist,Searchword,filecount,foundlist,hitcount,filetype,folder):
    for number in range(15):
        print("\n")
        if folder == "":
            cf = pathlib.Path(__file__).parent.resolve()
            cf = str(cf) + "/"
            folder = folder.replace("",f"{cf}")
        if "/" != folder:
            folder = folder+"/"
    for (dirpath, dirnames, filenames) in walk(folder):
        for x in filenames:
            if filetype in str(x):
                filelist.append(x)
            else:
                pass
        break
    for x in filelist:
        with open(f"{folder}{x}", "r") as Opened:
            reading = Opened.read()
            Opened.close()
            if Searchword in reading:
                foundlist.append(x)
                hitcount += 1
                filecount += 1
            else:
                filecount += 1
    print(f"BulkSearcher searched through {filecount} File's and found {hitcount} Hit's\n")
    t.sleep(1)
    for x in foundlist:
        t.sleep(1)
        print(f"{Searchword} Found in {x}")

    print("\nPress Enter to Exit...")
    while True:
        if kb.is_pressed("enter"):
            exit()
    else:
        print("\nPress Enter to Exit...")
        while True:
            if kb.is_pressed("enter"):
                exit()

def IterateOccurances(filelist, Searchword, filecount, foundlist, hitcount,filetype,folder):
    for number in range(15):
        print("\n")
        if folder == "":
            cf = pathlib.Path(__file__).parent.resolve()
            cf = str(cf) + "/"
            folder = folder.replace("",f"{cf}")
        if "/" != folder:
            folder = folder+"/"
    for (dirpath, dirnames, filenames) in walk(folder):
        for x in filenames:
            if filetype in str(x):
                filelist.append(x)
            else:
                pass
        break
    for x in filelist:
        with open(f"{folder}{x}", "r") as Opened:
            reading = Opened.read()
            Opened.close()
            if Searchword in reading:
                foundlist.append(x)
                hitcount += 1
                filecount += 1
            else:
                filecount += 1
    print(f"BulkSearcher searched through {filecount} File's and found {hitcount} Hit's\n")
    t.sleep(1)
    for x in foundlist:
        t.sleep(1)
        with open(f"{folder}{x}", "r") as Opened:
            reading = Opened.read()
            Opened.close()
        Rcount = reading.count(Searchword)
        print(f"{Searchword} Found in {x} [{Rcount} x]")
    print("\nPress Enter to Exit...")
    while True:
        if kb.is_pressed("enter"):
            exit()
    else:
        print("\nPress Enter to Exit...")
        while True:
            if kb.is_pressed("enter"):
                exit()




def Hotkeys(filelist,Searchword,filecount,foundlist,hitcount,filetype,folder):
    print(f"\nYour Keyword: {Searchword}, Your Filetype: {filetype}, Your Search-Folder: {folder}\n")
    print("\nPress 1 to BulkSearch files & specify in which files it is found.")
    print("\nPress 2 to BulkSearch files & specify how many times it occur's per found file.")
    while True:
        if kb.is_pressed("1"):
            IterateFiles(filelist, Searchword, filecount, foundlist, hitcount,filetype,folder)
            break
        if kb.is_pressed("2"):
            IterateOccurances(filelist, Searchword, filecount, foundlist, hitcount,filetype,folder)
            break

Hotkeys(filelist,Searchword,filecount,foundlist,hitcount,filetype,folder)
