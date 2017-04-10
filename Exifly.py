import os
import subprocess
from PIL import Image

File_Input = raw_input("Enter name of file (example.jpg) : ")
File_Display = Image.open(File_Input)
File_Display.show()
File_Subject = raw_input("Enter the photo's subject: ")
File_Location = raw_input("Enter a location tag: ")


def trim_filename(s, n):
        return s[n:]


def get_exif(input_name):
        exif_data = subprocess.check_output(["exiftool", input_name])
        exif = exif_data.splitlines()
        for item in exif:
                if 'Date/Time Original' in item:
                        filename = item
                        updatename = trim_filename(filename, 34)+' - '+File_Subject+' - ('+File_Location+')'
                        os.rename(os.path.abspath(File_Input), updatename)

get_exif(File_Input)
