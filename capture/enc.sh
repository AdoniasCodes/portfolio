#!/bin/zsh
# usage: enc.sh slug
F=/opt/homebrew/bin/ffmpeg; M=/Users/eyoel/vibecoding/job/websites-portfolio/media; R=/Users/eyoel/vibecoding/job/websites-portfolio/capture/raw/$1
S=$(cat $R/start.txt)
$F -y -loglevel error -ss $S -i $R/raw.webm -t 16 -vf "fps=30,scale=1280:800:flags=lanczos" -an -c:v libx264 -crf 28 -preset slow -pix_fmt yuv420p -movflags +faststart $M/$1.mp4
$F -y -loglevel error -i $M/$1.mp4 -c:v libvpx-vp9 -b:v 0 -crf 40 -row-mt 1 -an $M/$1.webm
$F -y -loglevel error -i $M/$1-top.png -vf scale=1440:900 -q:v 5 $M/$1.jpg
