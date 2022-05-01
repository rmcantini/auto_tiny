''' code from youtube '''
import os
import tinify


def compress_image(image_source, output_file_path):
    try:
        image_file_name = os.path.basename(image_source)

        if image_source.startswith('https'):
            source = tinify.from_url(image_source)

        else:
            source = tinify.from_file(image_source)
        print(f'{image_file_name} compressed successfully')
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


image_folder = os.path.join(os.getcwd(), 'Images')
output_folder = os.path.join(os.getcwd(), 'Outputs')

file1 = os.path.join(image_folder, 'rocky.jpg')
file2 = os.path.join(image_folder, 'thumbnail.png')
file3 = 'https://live.staticflickr.com/2861/32837141013_3e8f61402b_o_d.jpg'

API_KEY = '<API KEY>'
tinify.key = API_KEY
compress_image(file1, os.path.join(output_folder, '1.jpeg'))
compress_image(file2, os.path.join(output_folder, '2.jpeg'))
compress_image(file3, os.path.join(output_folder, '3.jpeg'))
