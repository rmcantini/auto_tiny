''' code from youtube tut '''
import json
import os
import tkinter
from tkinter.filedialog import askdirectory
import tinify

# intro explanation pop-up
tkinter.messagebox.showinfo(
    'info', 'Selecione a pasta com os arquivos para compressão.')

# asks what directory to work with
path_main = askdirectory(
    initialdir='~/downloads',
    title='Selecione a pasta onde estão os arquivos')
names = os.listdir(path_main)


def compress_image(image_source, output_file_path):
    ''' compress using tiny '''
    try:
        image_file_name = os.path.basename(image_source)

        if image_source.startswith('https'):
            source = tinify.from_url(image_source)
        else:
            source = tinify.from_file(image_source)
        print(f'{image_file_name} compressed successfully')

    except tinify.errors.AccountError:
        tkinter.messagebox.showinfo('info', 'Invalid API Key')
        return False

    except tinify.errors.ConnectionError:
        tkinter.messagebox.showinfo(
            'info', 'Please check your internet connection')
        return False

    except tinify.errors.ClientError:
        tkinter.messagebox.showinfo('info', 'File type is not supported')
        return False

    else:
        # export compressed image file
        source.to_file(output_file_path)
        print(f'File exported to {output_file_path}')
        return True


# finds the json API and reads it
os.chdir(r'G:\CODE\Tiny\.secrets')
API_KEY = json.loads(open('api_key.json', encoding='utf-8').read())['API_KEY']
tinify.key = API_KEY


def weight(each_file):
    ''' Get list of all files only in the given directory '''
    return os.path.isfile(os.path.join(path_main, each_file))


files_list = filter(weight, os.listdir(path_main))

# Create a list of files in directory along with the size
size_of_file = [
    (f, os.stat(os.path.join(path_main, f)).st_size)
    for f in files_list]

output_folder = os.path.join(path_main, 'output')

# Iterate over list of files along with size
for f, s in size_of_file:
    MAX_SIZE = 250000

    # Check if the file is too heavy
    if s >= MAX_SIZE:
        kb_size_file = s
        file_name = f
        # calls the damn thing
        compress_image(os.path.join(path_main, file_name),
                       os.path.join(output_folder, file_name))
    else:
        pass
        # print(f'no compress, {f}:{s}')

compressions_this_month = tinify.compression_count
tkinter.messagebox.showinfo(
    'info', f'Sucesso total. \nAquivos comprimidos: {compressions_this_month}, de 500.')
