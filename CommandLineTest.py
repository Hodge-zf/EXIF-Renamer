import os

exifAsDictionary = os.system("exiftool testimage.jpeg")
dict(item.split(":") for item in exifAsDictionary.split("/n"))
