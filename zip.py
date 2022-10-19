"""compressing all files to zip"""
import os
from shutil import make_archive

# from zipfile import ZipFile
import tkinter as tk

from tkinter.filedialog import askdirectory

# import zipfile

# hide root window
root = tk.Tk()
root.withdraw()

# intro explanation pop-up
tk.messagebox.showinfo("info", "Selecione a pasta com os arquivos para compressão.")

# asks what directory to work with (input)
path_main = askdirectory(
    initialdir="~/downloads", title="Selecione a pasta onde estão os arquivos"
)

FILE = "entrega"  # zip file name
DIRECTORY = os.chdir(path_main)  # folder with files (png's)
make_archive('arquivo', "zip", os.getcwd)

