#!/usr/bin/env python3
# coding:utf-8

from PIL import Image, ImageFont, ImageDraw

image = Image.open('SMTC01.png')
w, h = image.size
font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMono.ttf', 50)
draw = ImageDraw.Draw(image)
draw.text((4*w/5, h/5), '5', fill=(255, 10, 10), font=font)
image.save('SMTC0100.png', 'png')
