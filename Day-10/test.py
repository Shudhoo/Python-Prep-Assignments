# this is a example to list the files in the floders provided as input from the user!!

import os

folders = input("Provide list of folders with a single space !! :" ).split()

for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please provide a valid file name !! wrong folder name :", folder)
        continue
    except PermissionError:
        print("You dont have permission to open this file !!")
        continue
    print("-----------------This is the Floder name provided----------------------:", folder)
    for file in files:
        print(file)
