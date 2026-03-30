# 📂 File Organizer Script

## 📌 Overview

This Python script automatically organizes files in a specified directory into folders based on their file extensions. It helps keep your workspace clean by sorting files like images, videos, documents, and more into categorized folders.

---

## ⚙️ Features

* Prompts user to enter a directory path
* Validates if the directory exists
* Automatically creates folders if they don’t exist
* Sorts files into categories such as:

  * Music
  * Videos
  * Images
  * Documents
  * Applications
  * Archives
  * Programs
* Moves files into their respective folders

---

## 🛠️ Requirements

* Python 3.x
* No external libraries required (uses built-in modules: `os`, `shutil`)

---

## 🚀 How to Use

1. Run the script:

   ```bash
   python your_script_name.py
   ```

2. Enter the full directory path when prompted:

   ```
   Enter your directory path: C:\Users\YourName\Downloads
   ```

3. The script will:

   * Change to the specified directory
   * Scan all files
   * Move them into appropriate folders

---

## 📁 Supported File Types

| Extension                                  | Folder        |
| ------------------------------------------ | ------------- |
| .mp3                                       | music         |
| .mp4, .mkv, .avi, .mov, .wmv, .flv         | videos        |
| .jpg, .jpeg, .png, .gif, .bmp, .webp, .svg | images        |
| .txt                                       | files         |
| .pdf, .doc, .docx                          | documents     |
| .ppt, .pptx                                | presentations |
| .xls, .xlsx                                | spreadsheets  |
| .exe                                       | applications  |
| .zip                                       | archives      |
| .py                                        | programs      |

---

## ⚠️ Notes

* Existing folders will not be overwritten.
* Files with unsupported extensions will remain untouched.
* Make sure you have permission to access and modify the selected directory.

---

## 💡 Example

Before:

```
Downloads/
  song.mp3
  video.mp4
  image.jpg
  file.pdf
```

After running the script:

```
Downloads/
  music/
    song.mp3
  videos/
    video.mp4
  images/
    image.jpg
  documents/
    file.pdf
```

---

## 🧠 Future Improvements

* Add support for more file types
* GUI version (using Tkinter or PyQt)
* Option to copy instead of move files
* Logging system for tracking changes

---

## 👨‍💻 Author

Your Name Here

---

## 📜 License

This project is open-source and free to use.

