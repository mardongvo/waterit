#!/usr/bin/python3
import random
from PIL import Image, ImageDraw, ImageFont
import sys

if len(sys.argv) < 3:
    print("usage: waterit.py <sourcefile> <text>")
sourcefile = sys.argv[1]
text = sys.argv[2]
img = Image.open(sourcefile).convert("RGBA")

txt = Image.new('RGBA', img.size, (255,255,255,0))
draw = ImageDraw.Draw(txt)
width, height = img.size 

for i in range(20):
    #TODO: linux font
    font = ImageFont.truetype("arial.ttf", random.randint(20,40))
    x=random.randint(0, width)
    y=random.randrange(0,height)
    rgba = (random.randint(128,255), random.randint(128,255), random.randint(128,255), random.randint(50,100))
    draw.text((x,y), text, fill=rgba, font=font)

watermarked = Image.alpha_composite(img, txt)
watermarked.save(sourcefile+'_wm.png')
