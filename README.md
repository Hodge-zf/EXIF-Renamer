# Exifly

A small python executable that will allow the user to pass in a picture file, read the EXIF data, then rename the file in a manner that allows for easy sorting and quick user recognition.

Currently designed & tested for use on Linux/OS X with JPEG format, but potentially expandable for broader use.

## Depends on:

* [Python 2.7](https://www.python.org/download/releases/2.7/)
* Python [Pillow](https://python-pillow.org) (`PIL` fork) library
* Python [subprocess](https://docs.python.org/2/library/subprocess.html) module
* [exiftool](http://www.sno.phy.queensu.ca/~phil/exiftool/exiftool_pod.html)` command-line application
