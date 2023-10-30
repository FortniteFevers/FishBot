import requests
import pyfiglet
import time
import os
import PIL
from PIL import Image, ImageFont, ImageDraw

def solos(data, loadFont, background, x):
    
    CenterLine = 275

    # Writes Wins
    deaths = str(x['stats']['all']['solo']['wins'])
    font=ImageFont.truetype(loadFont,30)
    draw=ImageDraw.Draw(background)
    draw.text(
        (645.1,CenterLine),
        deaths,
        font=font,
        fill='white', 
        anchor='ms'
        )
    ########

    # Writes Matches
    matches = str(x['stats']['all']['solo']['matches'])
    font=ImageFont.truetype(loadFont,30)
    draw=ImageDraw.Draw(background)
    draw.text(
        (776.6,CenterLine),
        matches,
        font=font,
        fill='white', 
        anchor='ms'
        )
    ########

    # Writes Win %
    winp = round(x['stats']['all']['solo']['winRate'], 2)
    winp = str(winp) + '%'
    font=ImageFont.truetype(loadFont,30)
    draw=ImageDraw.Draw(background)
    draw.text(
        (921.2,CenterLine),
        winp,
        font=font,
        fill='white', 
        anchor='ms'
        )
    ########

    # Writes K/D
    kd = round(x['stats']['all']['solo']['kd'], 2)
    kd = str(kd)
    font=ImageFont.truetype(loadFont,30)
    draw=ImageDraw.Draw(background)
    draw.text(
        (1044.6,CenterLine),
        kd,
        font=font,
        fill='white', 
        anchor='ms'
        )
    ########

    # Writes Kills
    kills = str(x['stats']['all']['solo']['kills'])
    font=ImageFont.truetype(loadFont,30)
    draw=ImageDraw.Draw(background)
    draw.text(
        (1168.2,CenterLine),
        kills,
        font=font,
        fill='white', 
        anchor='ms'
        )
    ########

    # Writes KPM
    kpm = round(x['stats']['all']['solo']['killsPerMatch'], 2)
    kpm = str(kpm)
    font=ImageFont.truetype(loadFont,30)
    draw=ImageDraw.Draw(background)
    draw.text(
        (1290.7,CenterLine),
        kpm,
        font=font,
        fill='white', 
        anchor='ms'
        )
    ########

    # Writes Deaths
    deaths = str(x['stats']['all']['solo']['deaths'])
    font=ImageFont.truetype(loadFont,30)
    draw=ImageDraw.Draw(background)
    draw.text(
        (1416.3,CenterLine),
        deaths,
        font=font,
        fill='white', 
        anchor='ms'
        )
    ########