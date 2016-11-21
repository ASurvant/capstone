# Anthony Survant
# Capstone Spring 2013

import os
import PIL
import Image
import math


def v(fname):
#	ffmpeg -i FILENAME -s qvga image%d.jpg
#	os.system("rm image*.jpg")
#	os.system("ffmpeg -i "+fname+" image%d.jpg")

	avgrows=loadImage("image34.jpg")
	
	imagenumber = 34
	fullscreen=[]
	while True:
		print imagenumber
		try:
			column = loadImage("image"+str(imagenumber)+".jpg")
		except IOError:
			break
		fullscreen+=[column]
		imagenumber+=1
	dumpfile(fullscreen)

# load pixels in from filename, return a vertical line of average of rows
def loadImage(filename):
	im=Image.open(filename).convert('RGB')
	width,height=im.size
	
	screenshot = [0]*width
	for i in xrange(width):
		screenshot[i]=[0]*height
	
	for x in xrange(width):
		for y in xrange(height):
			screenshot[x][y]=im.getpixel((x,y))

#	print avgrgb(screenshot[0])
#	print avgrgb(getrow(screenshot,0))
	
	avgrows = [0] * height
	
	for row in xrange(height):
		avgrows[row] = avgrgb(getrow(screenshot, row))
#	print avgrows

	return avgrows
	
def dumpfile(screenshot):
	width,height=len(screenshot),len(screenshot[0])
	f= file("image.txt","w")
	f.write(str(width)+" "+str(height)+" ")
	for x in xrange(width):
		for y in xrange(height):
			f.write(str(screenshot[x][y][0])+" "+str(screenshot[x][y][1])+" "+str(screenshot[x][y][2])+" ")
	f.close()

def getrow(screenshot, r):
	w,h = len(screenshot),len(screenshot[0])
	row = [0] * w
	for i in xrange(w):
		row[i] = screenshot[i][r]
	return row

def avgrgb(pixels):
	redsum,greensum,bluesum = 0,0,0
	for pixel in pixels:
		redsum += pixel[0]
		greensum += pixel[1]
		bluesum += pixel[2]
	redsum /= len(pixels)
	greensum /= len(pixels)
	bluesum /= len(pixels)
	
	return (redsum,greensum,bluesum)

def correct():
	f = open('image.txt','r').read().split(" ")
	w = int(f[0])
	h = int(f[1])
	f = f[2:]
	image = [0] * w
	for x in xrange(w):
		image[x] = [0]*h
		for y in xrange(h):
			image[x][y] = (int(f[x*h*3+y*3]),int(f[x*h*3+y*3+1]),int(f[x*h*3+y*3+2]))
		
#	print image[0:2]
	return image

def change(image):
	last = [(0,0,0),(0,0,0),(0,0,0),(0,0,0)]
	seconds = 0
	for x in image:
		seconds += 1
		y = avgrgb(x)
		r = y[0]
		g = y[1]
		b = y[2]
		last.append(y)
		last = last[1:]
		first = avgrgb(last[:2])
		second = avgrgb(last[2:])
		threshold = 30
		#print first,second
		if abs(first[0]-second[0]) > threshold or abs(first[1]-second[1]) > threshold or abs(first[2]-second[2]) > threshold:
			print seconds, " Found a transition."
			last = last[2:]
			last = last * 2
	

# v("v1.avi")
change(correct())
# r*256*256 + g*256 + b

# Typecast as char
# ffmpeg -i movie.mp4 -r 1 -s 240x100 image%d.jpg
