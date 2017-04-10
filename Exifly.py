import os,sys
from PIL import Image
from PIL.ExifTags import TAGS

img = Image.open('testimage.jpg')

def get_exif(imagename):

    filename.show()
    exifAsDictionary = {}
    info = filename._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        exifAsDictionary[decoded] = value
    return exifAsDictionary

get_exif(filename)