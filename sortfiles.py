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

#print(files)

# for f in files:
#     if ((f.find("THM")) == -1):
#         continue
#     else:
#         print("File: {}", f)

for f in files:
    if ((thm in f) or (THM in f)):
        print("File: {}", f)
    else:
        print("Normal file: {}", f)
