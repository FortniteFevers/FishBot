import requests
import pyfiglet
import time
import os
import PIL
from PIL import Image, ImageFont, ImageDraw

def other(data, loadFont, background, x):

    bpinfocenter = 255

    ltminfocenter = 461
    
    
    # Writes Battle Pass Stuff
    deaths = str(x['battlePass']['level'])
    font=ImageFont.truetype(loadFont,30)
    draw=ImageDraw.Draw(background)
    draw.text(
        (1611.6,bpinfocenter),
        deaths,
        font=font,
        fill='white', 
        anchor='ms'
        )

    deaths = str(x['battlePass']['progress']) + '%'
    font=ImageFont.truetype(loadFont,30)
    draw=ImageDraw.Draw(background)
    draw.text(
        (1758.3,bpinfocenter),
        deaths,
        font=font,
        fill='white', 
        anchor='ms'
        )
    ########

    # LTM STUFF

    if x['stats']['all']['ltm'] != None:
        text = str(x['stats']['all']['ltm']['wins'])
        font=ImageFont.truetype(loadFont,30)
        draw=ImageDraw.Draw(background)
        draw.text(
            (1611.6,ltminfocenter),
            text,
            font=font,
            fill='white', 
            anchor='ms'
            )

        text = str(x['stats']['all']['ltm']['matches'])
        font=ImageFont.truetype(loadFont,30)
        draw=ImageDraw.Draw(background)
        draw.text(
            (1758.3,ltminfocenter),
            text,
            font=font,
            fill='white', 
            anchor='ms'
            )