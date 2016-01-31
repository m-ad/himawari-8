
Prerequisites:
Python 2.7 with PIL and requests
ffmpeg


STEP 1: GET THE IMAGES
Open and edit fetch_many.py. Especially select the zoom and directory where the images should be saved. The directory has to end with a '/' and has to exist already. Execute this script with python and wait until it's done.

STEP 2: INTERPOLATE GAPS
This substitutes the "no image"-images at 14:40 and 2:40 with an interpolation of the images before and after the gap. Open and edit interp.py. The settings should match those from step 1.

STEP 3: DRAW TIMESTAMP AND RENAME
Open and edit label_and_rename.py. Here you can determine how the timestamp should look. The images will be saved as "image1.png", "image2.png", because that makes life easier for step 4.

STEP 4: GENERATE THE GIF
If your are on Windows, open and edit makegif.bat. If you use Linux, it should be fairly straigthforward to rewrite this into a shell script. Set the directory names you used in the previous steps. Make sure the scale is right (multiply the zoomlevel of step 1 with 550 to get the correct scale).  Run this script and enjoy your GIF!
