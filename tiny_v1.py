''' code from youtube tut '''
import json
import os
import tinify


def compress_image(image_source, output_file_path):
    ''' compress using tiny '''
    try:
        source = tinify.from_url(image_source)
        source = tinify.from_file(image_source)

    except tinify.errors.AccountError:
        print('Invalid API Key')
        return False
    except tinify.errors.ConnectionError:
        print('Please check your internet connection')
        return False
    except tinify.errors.ClientError:
        print('Files type os not supported')
        return False

    else:
        # export compressed image file
        source.to_file(output_file_path)
        print(f'File exported to {output_file_path}')
        return True


# defines the input and output folders (change for an tkinter askfolder)
image_folder = os.path.join(os.getcwd(), 'files')
# changed to same as input folder
output_folder = os.path.join(os.getcwd(), 'Outputs')

# defines which  files to use (change to a for loop that gets all files bigger than 250kb)
file1 = os.path.join(image_folder, '2213_super_voxus_728x90.png')
file2 = os.path.join(image_folder, '2213_super_voxus_336x280.png')

# finds the json API and reads it
os.chdir(r'G:\CODE\Tiny\.secrets')
API_KEY = json.loads(open('api_key.json', encoding='utf-8').read())['API_KEY']
tinify.key = API_KEY

# calls the compressing
compress_image(file1, os.path.join(output_folder, '01.png'))
compress_image(file2, os.path.join(output_folder, '02.png'))
