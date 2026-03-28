import os
import shutil

import os

mydir = input("Enter your directory path: ").strip()

if os.path.isdir(mydir):
    try:
        os.chdir(mydir)
        print("Changed directory successfully")
    except PermissionError:
        print("Permission denied")
else:
    print("Invalid directory")

folders={
  ".mp3": "music",
  ".mkv": "videos",
  ".avi": "videos",
  ".mov": "videos",
  ".wmv": "videos",
  ".flv": "videos",
  ".mp4": "videos",
  ".jpg": "images",
  ".jpeg": "images",
  ".png": "images",
  ".gif": "images",
  ".bmp": "images",
  ".webp": "images",
  ".svg": "images",
  ".txt": "files",
  ".pdf": "documents",
  ".exe": "applications",
  ".zip": "archives",
  ".doc": "documents",
  ".docx": "documents",
  ".ppt": "presentations",
  ".pptx": "presentations",
  ".xls": "spreadsheets",
  ".xlsx": "spreadsheets",
  ".py": "programs"
}

for file in os.listdir():
  if os.path.isfile(file):
    name , ext = os.path.splitext(file)
    ext = ext.lower()

    if ext in folders:
      folder=folders[ext]

      os.makedirs(folder,exist_ok=True)

      shutil.move(file,folder)
      print("changed sucessfully")