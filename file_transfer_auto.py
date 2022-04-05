import shutil
import os
import datetime as datetime
from datetime import timedelta
import time

# path of source folder location
source = "C:/Users/scpog/Desktop/FolderX/"

# path of destination folder location 
destination = "C:/Users/scpog/Desktop/FolderY/"
files = os.listdir(source)
secondsintheday = 24*60*60
now = time.time()
before = now - secondsintheday


 # move files represented by 'i' to destination folder
def FileTransfer():
    for i in files:
        filepath = os.path.join(source, i)
        modTime = os.path.getmtime(filepath)
        if modTime > before:
            destPath = os.path.join(destination, i)
            shutil.move(filepath, destPath)
   
FileTransfer()