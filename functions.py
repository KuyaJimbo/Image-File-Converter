import os
from PIL import Image

# resize the image to smaller size while maintaining aspect ratio
# by default, the width and height are set to 500 pixels
def resize_image(img, selected_size, width=500, height=500):
    # resize the image to smaller size while maintaining aspect ratio
    if selected_size == "1":
        img.thumbnail((500, 500))
    elif selected_size == "2":
        img.thumbnail((1000, 1000))
    elif selected_size == "3":
        img.thumbnail((1500, 1500))
    elif selected_size == "4":
        img.thumbnail((int(width), int(height)))
    return img

# convert the image to the selected file type

def convert_image(output_folder, img, filename, file_type):
    clean_name = os.path.splitext(filename)[0]

    if file_type == "1":
        img.save(f'{output_folder}{clean_name}.png', 'png')
    elif file_type == "2":
        img.save(f'{output_folder}{clean_name}.jpg', 'jpeg')
    elif file_type == "3":
        img.save(f'{output_folder}{clean_name}.bmp', 'bmp')

    # confirm the conversion
    print(f'Converted {filename}')
    return