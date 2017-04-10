import os
import subprocess
from PIL import Image

fileinput = raw_input("Enter name of file (example.jpg) : ")
filedisp = Image.open(fileinput)
filedisp.show()
filesubject = raw_input("Enter the photo's subject: ")
filelocation = raw_input("Enter a location tag: ")




def trim_filename(s,n):
        return s[n:]


def get_exif(inputname):
        exifdata = subprocess.check_output(["exiftool", inputname])
        exif = exifdata.splitlines()
        for item in exif:
                if 'Date/Time Original' in item:
                        filename = item
                        updatename = trim_filename(filename,34)+' - '+filesubject+' - '+filelocation
                        os.rename(fileinput, updatename)

get_exif(fileinput)