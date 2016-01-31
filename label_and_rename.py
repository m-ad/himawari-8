# take a directory of Himawari-8 images 2015-12-01T02-30-00_z1.png, 2015-12-01T02-40-00_z1.png,...
# draw a timestamp on them
# save them as image1.png, image2.png,...

from os import listdir
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# define input and output directory
inputdir	=	'testday1/'
outputdir	=	'labeled2/'

files 	=	listdir(inputdir)
i		=	0
font	=	ImageFont.truetype("verdana.ttf",10)

for file in files:
	i+=1
	im=Image.open(inputdir+file)
	draw = ImageDraw.Draw(im)
	
	# make text to draw on image
	text='Himawari-8\n'+file.replace('-00_z1.png','').replace('T',' ')
	text=text[:-3]+':'+text[-2:]
	
	draw.text((0, 520),text,(30,70,110),font=font)
	
	im.save(outputdir+'image'+str(i)+'.png')