''' Script to select only files with a specific size in a folder '''
import os
import tkinter
from tkinter.filedialog import askdirectory

# intro explanation pop-up
tkinter.messagebox.showinfo(
    'info', 'Selecione a pasta com os desdobramentos a serem organizados.')

# asks what directory to work with
path_main = askdirectory(
    initialdir='~/downloads',
    title='Selecione a pasta onde estão os arquivos')
names = os.listdir(path_main)


def weight(each_file):
    ''' Get list of all files only in the given directory '''
    return os.path.isfile(os.path.join(path_main, each_file))


files_list = filter(weight, os.listdir(path_main))

# Create a list of files in directory along with the size
size_of_file = [
    (f, os.stat(os.path.join(path_main, f)).st_size)
    for f in files_list]

# Iterate over list of files along with size
for f, s in size_of_file:
    MAX_SIZE = 250000

    # Check if the file is too heavy
    if s >= MAX_SIZE:
        print(f'Found, {f}: {s}')
    else:
        print(f'no compress, {f}:{s}')
