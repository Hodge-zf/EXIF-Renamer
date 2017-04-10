from PIL import Image
import piexif


imagename = 'someimage.jpeg'

filename = Image.open(imagename)
filename.show()
exif_dict = piexif.load(filename.info['resolution'])
exif_bytes = piexif.dump(exif_dict)
print exif_bytes
