from PIL import Image, ImageOps
import sys
import os


""" Check for errors """
# Check if there are exactly 3 arguments
if len(sys.argv) != 3:
    sys.exit("Need 2 images")
# Get the file extentions
path1 = os.path.splitext(sys.argv[1])[1].lower()
path2 = os.path.splitext(sys.argv[2])[1].lower()
# Check if the file is a .jpg, .jpeg, or .png
if path1 != ".jpg" and path1 != ".jpeg" and path1 != ".png":
    sys.exit("Image has to be .jpg, .jpeg, or .png")
# Check if both the files are the same type
if path1 != path2:
    sys.exit("File extentions need to match")


""" Change the image """
# Open the image
with Image.open(sys.argv[1]) as img, Image.open("shirt.png") as shirt:
    # Fit the shirt to the img and then put it on there
    img = ImageOps.fit(img, shirt.size)
    img.paste(shirt, shirt)
    img.save(sys.argv[2])
