## Himawari-8 GIF animation

These are some scripts to generate Himawari-8 GIFs using `python` and `ffmpeg`.

Here is an example of the output you can expect: https://imgur.com/Zonhp5y

Original idea: https://gist.github.com/celoyd/b92d0de6fae1f18791ef

The main difference between the original and this version is that this version works on Windows because it is almost entirely written in `python`. For generating the GIF from the image sequence, `ffmpeg` is called from a very simple batch file, that can be rewritten as a shell script for Linux users. 

These scripts are comptible with `python 2.7`. For an updated version that is compatible with `python 3.6+`, see [this fork](https://github.com/ZeitOnline/himawari-8).

## Prerequisites:
- `python 2.7` with `PIL` and `requests`
- `ffmpeg`


## Step 1: Get the images
Open and edit `fetch_many.py`. Especially select the zoom and directory where the images should be saved. The directory has to end with a '/' and has to exist already. Execute this script with python and wait until it's done.

## Step 2: Interpolate gaps
This substitutes the "no image"-images at 14:40 and 2:40 with an interpolation of the images before and after the gap. Open and edit `interp.py`. The settings should match those from step 1.

## Step 3: Draw timestamp and rename
Open and edit `label_and_rename.py`. Here you can determine how the timestamp should look. The images will be saved as "image1.png", "image2.png", because that makes life easier for step 4.

## Step 4: Generate GIF
If your are on Windows, open and edit `makegif.bat`. If you use Linux, it should be fairly straigthforward to rewrite this into a shell script. Set the directory names you used in the previous steps. Make sure the scale is right (multiply the zoomlevel of step 1 with 550 to get the correct scale).  Run this script and enjoy your GIF!
