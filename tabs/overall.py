import requests
import pyfiglet
import time
import os
import PIL
from PIL import Image, ImageFont, ImageDraw

def overall(data, loadFont, background, x):
    # Writes Title
    name = data['data']['account']['name']
    name = name.upper()
    font=ImageFont.truetype(loadFont,35)
    w,h=font.getsize(name)
    draw=ImageDraw.Draw(background)
    draw.text(
        (297,280),
        name,
        font=font,
        fill='white', 
        anchor='ms'
        )
    ########

    # TOP - 410

    # Writes Deaths
    deaths = str(x['stats']['all']['overall']['deaths'])
    font=ImageFont.truetype(loadFont,25)
    draw=ImageDraw.Draw(background)
    draw.text(
        (146,410),
        deaths,
        font=font,
        fill='white', 
        anchor='ms'
        )
    ########

    # Writes Win %
    winp = round(x['stats']['all']['overall']['winRate'], 2)
    winp = str(winp) + '%'
    font=ImageFont.truetype(loadFont,25)
    draw=ImageDraw.Draw(background)
    draw.text(
        (296.5,410),
        winp,
        font=font,
        fill='white', 
        anchor='ms'
        )
    ########

    # Writes KD
    kd = round(x['stats']['all']['overall']['kd'], 2)
    kd = str(kd)
    font=ImageFont.truetype(loadFont,25)
    draw=ImageDraw.Draw(background)
    draw.text(
        (455.9,410),
        kd,
        font=font,
        fill='white', 
        anchor='ms'
        )
    ########

    # BOTTOM - 520.3

    # Writes KPM
    kpm = round(int(x['stats']['all']['overall']['killsPerMatch']), 2)
    kpm = str(kpm)
    font=ImageFont.truetype(loadFont,25)
    draw=ImageDraw.Draw(background)
    draw.text(
        (146,520.3),
        kpm,
        font=font,
        fill='white', 
        anchor='ms'
        )
    ########

    # Writes KILLS
    kills = str(x['stats']['all']['overall']['kills'])
    font=ImageFont.truetype(loadFont,25)
    draw=ImageDraw.Draw(background)
    draw.text(
        (296.5,520.3),
        kills,
        font=font,
        fill='white', 
        anchor='ms'
        )
    ########

    # Writes matches
    kills = str(x['stats']['all']['overall']['matches'])
    font=ImageFont.truetype(loadFont,25)
    draw=ImageDraw.Draw(background)
    draw.text(
        (455.9,520.3),
        kills,
        font=font,
        fill='white', 
        anchor='ms'
        )
    ########

    # Writes wins
    wins = str(x['stats']['all']['overall']['wins'])
    font=ImageFont.truetype(loadFont,40)
    draw=ImageDraw.Draw(background)
    draw.text(
        (296.5,655),
        wins,
        font=font,
        fill='white', 
        anchor='ms'
        )
    ########