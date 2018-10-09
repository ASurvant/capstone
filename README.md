# Movie Barcode Generator
This was my capstone project for my Minor in Computer Science at American University. The barcode is generated from a film I directed a year earlier (2012) in Prague: https://youtu.be/ldON19zXWgA


![Image of Original](https://raw.githubusercontent.com/ASurvant/capstone/master/original.jpg)

### Requirements:
- Python 2.5
- PIL\*
- FFmpeg

### Usage:
When called, Capstone.py will break a video file into frames at the interval of your choice. The barcode generated below used 1 second of video == 1 vertical pixel. Those frames will be saved into an Image.txt as RGB values.

The included Java file will convert the Image.txt into a barcode.

![Image of Barcode](https://raw.githubusercontent.com/ASurvant/capstone/master/barcode.jpg)

\* *note: I wrote this as a student in 2013. It used Python Imaging Library, which is mostly abandoned now. If you want a barcode generator of your own using Python, I suggest looking into Pillow. Also, I know my Python syntax is suppsoed to be snake_case, so forgive the noobie me who wrote this.*
