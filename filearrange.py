import os
import shutil

os.chdir('C:/Users/user/OneDrive/Desktop/test/')

folders={
  ".mp3": "music",
  ".mp4": "videos",
  ".txt": "files",
  ".pdf": "PDF_Documents"
}

for file in os.listdir():
  if os.path.isfile(file):
    print("file exists")
    name , ext = os.path.splitext(file)

    if ext in folders:
      folder=folders[ext]

      os.makedirs(folder,exist_ok=True)

      shutil.move(file,folder)