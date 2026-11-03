#!/bin/zsh
M=/Users/eyoel/vibecoding/job/websites-portfolio/media; D=$(/opt/homebrew/bin/ffprobe -v error -show_entries format=duration -of csv=p=0 $M/$1.mp4)
echo $1 $D $(/opt/homebrew/bin/ffprobe -v error -show_entries stream=width,height -of csv=p=0 $M/$1.mp4) $(stat -f%z $M/$1.mp4)
for p in 25 50 75; do /opt/homebrew/bin/ffmpeg -y -loglevel error -ss $(echo "$D*$p/100"|bc -l) -i $M/$1.mp4 -frames:v 1 -vf scale=640:-1 frames/$1-$p.jpg; done
