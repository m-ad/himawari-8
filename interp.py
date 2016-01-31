from PIL import Image

def interp(imfile1,imfile2,imfileout,alpha=0.5):
	im1	=	Image.open(imfile1)
	im2	=	Image.open(imfile2)
	im3	=	Image.blend(im1,im2,alpha)
	im3.save(imfileout)	# filetype is determined by extension
	
def strpad(i):
	if i<10:
		return '0'+str(i)
	else:
		return str(i)
	
dir		= 'testz1/'
	
year	= 2015
month	= 12
days	= range(1,32)
hours	= range(0,24)
minutes	= [10*x for x in range(0,6)]

for day in days:
	for hour in hours:
		for minute in minutes:			
			if (hour==2 or hour==14) and minute==40:
				filenamebase = dir+str(year)+'-'+strpad(month)+'-'+strpad(day)+'T'+strpad(hour)+'-'
				filename30 = filenamebase+'30-00_z1.png'
				filename40 = filenamebase+'40-00_z1.png'
				filename50 = filenamebase+'50-00_z1.png'
				interp(filename30,filename50,filename40)
				print('Fixed '+filename40)
