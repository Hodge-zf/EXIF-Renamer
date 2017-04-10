import os

exifAsDictionary = os.system("exiftool someimage.jpeg")
dict(item.split(":") for item in exifAsDictionary.split("/n"))



