# Summary:
# This program will convert all images in a folder to a specified file type and size.
# Please put your image(s) in the "Input_Folder" before running the program.
# This program will create the "Output_Folder" if it does not exist.
# The converted images will be saved to the "Output_Folder"

# This program requires the Pillow library to be installed.
# To install Pillow, run the following command in the terminal:
# pip install Pillow

#---------------------------------------------#

# for file handling
import os
# for image handling
from PIL import Image

# import functions from functions.py
from functions import resize_image, convert_image

# Set the Input and Output Folders
image_folder = "Input_Folder/"
output_folder = "Output_Folder/"

# Check if the Output Folder exists, if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#---------------------------------------------#

# Create the Menu:
print("Welcome to the Image File Converter")

# Get the User Input for the File Type
print("Please select a file type to convert to:")
print("1. PNG")
print("2. JPG")
print("3. BMP")
print("4. Need help deciding?")

# (use input validation)
file_type = input("Enter your selection: ")
while file_type not in ["1", "2", "3"]:
    if file_type == "4":
        print("PNG is a lossless format, supports transparency, and is the most commonly used format for images on the web.")
        print("JPG provides a good balance between file size and image quality, and is the most commonly used format for digital photos.")
        print("BMP is a lossless format, but the file size is very large. It is not commonly used for images on the web.")
        print()
    else:
        print("Invalid Selection, please try again.")
    file_type = input("Enter your selection: ")

# Confirm the User Input
print("You selected: " + file_type)
print()

#---------------------------------------------#

# Get User Input for the image size
print("Please select an image size:")
print("1. Small (500 pixels)")
print("2. Medium (1000 pixels)")
print("3. Large (1500 pixels)")
print("4. Custom")

# (use input validation)
selected_size = input("Enter your selection: ")
while selected_size not in ["1", "2", "3", "4"]:
    print("Invalid Selection, please try again.")
    selected_size = input("Enter your selection: ")

# Confirm the User Input
print("You selected: " + selected_size)
print()

# If the User wants a Custom Size, get the input as width and height
if selected_size == "4":
    width = input("Enter the width in pixels: ")
    while not width.isdigit():
        print("Invalid Selection, please try again.")
        width = input("Enter the width in pixels: ")
    
    height = input("Enter the height in pixels: ")
    while not height.isdigit():
        print("Invalid Selection, please try again.")
        height = input("Enter the height in pixels: ")
    
    # Confirm the User Input
    print("You selected: " + width + " x " + height)
    print()

#---------------------------------------------#

# Convert the User Input to the correct file type
for filename in os.listdir(image_folder):
    # open the image
    img = Image.open(f'{image_folder}{filename}')

    # resize the image to smaller size while maintaining aspect ratio
    img = resize_image(img, selected_size)

    # convert the image to the selected file type
    convert_image(output_folder, img, filename, file_type)

#---------------------------------------------#

# Confirm the conversion
print("All done!")
print("The converted images are saved to the Output Folder.")