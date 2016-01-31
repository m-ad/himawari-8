# This script is based on https://gist.github.com/celoyd/39c53f824daef7d363db

import requests as req
import sys
from dateutil.parser import parse
from PIL import Image
from StringIO import StringIO

# hi8-fetch.py <date> <zoom level> <output>
# E.g.: hi8-fetch.py 2016-01-13T22:10:00 8 2016-01-13T221000-z8.png
# Fetch Himawari-8 full disks at a given zoom level.
# Valid zoom levels seem to be powers of 2, 1..16, and 20.
#
# To do:
# - Better errors (e.g., catch the "No Image" image).
# - Don't ignore seconds, and/or:
# - option to snap to nearest valid time.
# - Librarify.

def fetch(date,zoom,output):

	# Tile size for this dataset:
	width = 550
	height = 550


	time = parse(date)
	scale = int(zoom)
	out = output
	# time = parse(sys.argv[1])
	# scale = int(sys.argv[2])
	# out = sys.argv[3]


	base = 'http://himawari8.nict.go.jp/img/D531106/%sd/550' % (scale)

	tiles = [[None] * scale] * scale


	def pathfor(t, x, y):
	  return "%s/%s/%02d/%02d/%02d%02d00_%s_%s.png" \
	  % (base, t.year, t.month, t.day, t.hour, t.minute, x, y)


	sess = req.Session() # so requests will reuse the connection
	png = Image.new('RGB', (width*scale, height*scale))

	for x in range(scale):
	  for y in range(scale):
		# print(str(x*scale+y+1) + " of " + str(scale*scale))
		path = pathfor(time, x, y)
		# print("fetching %s" % (path))
		tiledata = sess.get(path).content
		tile = Image.open(StringIO(tiledata))
		
		png.paste(tile, (width*x, height*y, width*(x+1), height*(y+1)))

	png.save(out, 'PNG')