import hi8fetch as hi8

def strpad(i):
	if i<10:
		return '0'+str(i)
	else:
		return str(i)

zoom 	= 1

dir		= 'testz1/'

year	= 2015
month	= 12
days	= range(21,32)
hours	= range(0,24)
minutes	= [10*x for x in range(0,6)]

for day in days:
	for hour in hours:
		for minute in minutes:
			namestr = str(year)+'-'+strpad(month)+'-'+strpad(day)+'T'+strpad(hour)+':'+strpad(minute)+':00'
			filename = dir+namestr.replace(':','-')+'_z'+str(zoom)+'.png'
			print(namestr)
			hi8.fetch(namestr,zoom,filename)