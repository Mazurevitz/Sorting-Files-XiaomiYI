import shutil
import os

#source = 'C:\\Users\\Wojtek\\Desktop\\100MEDIA'
#dest = 'C:\\Users\\Wojtek\\Desktop\\100MEDIA\\main'

source = os.path.join("C:", "Users", "Wojtek", "Desktop", "100MEDIA")
dest = os.path.join("C:", "Users", "Wojtek", "Desktop", "100MEDIA", "main")

#print(source)
#print(dest)

files = os.listdir(source)

thm = "thm"
THM = "THM"


for f in files:
    if ((thm in f) or (THM in f) or ("main" in f)):
        print(f"File: {f}")
    else:
        print(f"\tDesired file: {f}")
        shutil.move(source + "\\" + f, dest)
