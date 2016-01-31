@ echo off
REM For explanations see http://blog.pkh.me/p/21-high-quality-gif-with-ffmpeg.html
SET inputdir=labeled2/
SET out=testz1_1day.gif
SET palette=palette.png
SET filters=fps=24,scale=550:-1:flags=lanczos
ffmpeg -v warning -f image2 -i %inputdir%image%%d.png -vf "%filters%,palettegen" -y %palette%
ffmpeg -v warning -f image2 -i %inputdir%image%%d.png -i %palette% -lavfi "%filters% [x]; [x][1:v] paletteuse" -y %out%