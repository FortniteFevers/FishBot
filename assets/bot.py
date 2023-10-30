import requests
import time
from colorama import *
init()
import PIL
from PIL import Image, ImageDraw, ImageFont
from merge import merger
import tweepy
import os
import shutil

#===================#
#apiurl = 'https://benbot.app/api/v1/aes'
apiurl = 'https://pastebin.com/raw/956gf6hM'

delay = 10 # BOT DELAY IN SECONDS
lang = 'en' # LANGUAGE
watermark = 'FeversBot' # WATERMARK TO BE PLACED ON ICON
useFeaturedIfAvaliable = 'True' 
imageFont = 'BurbankBigCondensed-Black.otf' # FONT IMAGE USES
showitemsource = 'True' # SHOWS GAMEPLAY TAG

mergewatermark = '' # ADDS WATERMARK ON MERGED IMAGE

# API KEYS #
twitAPIKey = 'YMIHZ1YlpYFDndGwljfo4obEc'
twitAPISecretKey = 'hVd7mIDwTHqZX9FFZtnLSDQjnMD6bKCruXkGDgoaRwbVG6ZPrm'
twitAccessToken = '1057364060390543361-urr90UQRBNuu1Ggb8fXSMFlPWYDcw9'
twitAccessTokenSecret = '3XYUhKvWV9sWC3qnBfdc5gku3QoMDt4oDAJ8HcZvZfnmt'

#===================#

print('Starting bot...')

centerline = 256
data = requests.get('https://benbot.app/api/v1/status')
seasonnum = data.json()['currentFortniteVersionNumber']
auth = tweepy.OAuthHandler(twitAPIKey, twitAPISecretKey)
auth.set_access_token(twitAccessToken, twitAccessTokenSecret)
api = tweepy.API(auth)



def test():
    count = 1

    response = requests.get(apiurl)
    try:
        aesData = response.json()['dynamicKeys']
    except:
        return test()
    
    try:
        shutil.rmtree('icons')
        os.makedirs('icons')
    except:
        os.makedirs('icons')

    while 1:
        if response:
            try:
                response = requests.get(apiurl)
            except:
                return test()
            try:
                aesDataLoop = response.json()['dynamicKeys']
            except:
                return test()
            #aesDataLoop.raise_for_status()  # raises exception when not a 2xx response
            print("Checking for a new Dynamic Pak(s)... ("+str(count)+")")
            count = count + 1
            counter = 0
            if aesData != aesDataLoop:
                for i in aesDataLoop:
                    if not i in aesData:
                        print('\n--- NEW DATA FOUND ---\n')
                        pak = i
                        if 'optional' in pak:
                            pak = pak.replace('FortniteGame/Content/Paks/pakchunk', '').replace('optional-WindowsClient.pak', '')
                        else:
                            pak = pak.replace('FortniteGame/Content/Paks/pakchunk', '').replace('-WindowsClient.pak', '')
                        
                        # Generation:
                        response = requests.get(f'https://benbot.app/api/v1/cosmetics/br/dynamic/{pak}?lang={lang}')
                        try:
                            if response.json()['error'] == 'Pak file could not be found':
                                api.update_status(f'A pak has been decrypted, but an error has occured.')
                                print('ERROR')
                                test()
                        except:
                            pass
                        paknum = len(response.json())
                        print(f'Found {paknum} items in Pak{pak}')
                        if paknum == 0:
                            print('Pak has 0 cosmetics.')
                            api.update_status(f'Pak {pak} has been decrypted, however it has no items inside of it.')
                            return test()
                            
                        for i in response.json():
                            name = i['name']
                            id = i['id']
                            description = i['description']
                            backendtype = i['backendType']
                            if backendtype == 'AthenaCharacter':
                                backendtype = 'OUTFIT'
                            elif backendtype == 'AthenaBackpack':
                                backendtype = 'BACKPACK'
                            elif backendtype == 'AthenaDance':
                                backendtype = 'EMOTE'
                            elif backendtype == 'AthenaPickaxe':
                                backendtype = 'PICKAXE'
                            elif backendtype == 'AthenaLoadingScreen':
                                backendtype = 'LOADING SCREEN'
                            elif backendtype == 'AthenaItemWrap':
                                backendtype = 'WRAP'
                            else:
                                backendtype = 'N/A'
                            backendtype = backendtype.upper()

                            if useFeaturedIfAvaliable == 'True':
                                if i["icons"]["featured"] != None:
                                    url = i["icons"]["featured"]
                                else:
                                    if i['icons']['icon'] != None:
                                        url = i['icons']['icon']
                                    else:
                                        url = 'https://i.ibb.co/KyvMydQ/do-Not-Delete.png'
                            else:
                                if i['icons']['icon'] != None:
                                    url = i['icons']['icon']
                                else:
                                    url = 'https://i.ibb.co/KyvMydQ/do-Not-Delete.png'
                            try:
                                r = requests.get(url)
                            except:
                                print('a')
                            open(f'cache/{id}temp.png', 'wb').write(r.content)
                            iconImg = Image.open(f'cache/{id}temp.png')
                            iconImg.resize((512,512),PIL.Image.ANTIALIAS)


                            rarity = i["rarity"]
                            rarity = rarity.lower()
                            if i['series'] != None:
                                try:
                                    series = i['series']['name']
                                    if series == 'Icon Series':
                                        rarity = 'icon'
                                    elif series == 'MARVEL SERIES':
                                        rarity = 'marvel'
                                    elif series == 'Gaming Legends Series':
                                        rarity = 'gaminglegends'
                                    elif series == 'DC SERIES':
                                        rarity = 'dc' 
                                    elif series == 'Lava Series':
                                        rarity = 'lava'
                                    elif series == 'Shadow Series':
                                        rarity = 'shadow'
                                    elif rarity == 'Star Wars Series':
                                        rarity = 'starwars'
                                    elif rarity == 'Slurp Series':
                                        rarity = 'slurp'
                                    elif rarity == 'DARK SERIES':
                                        rarity = 'dark'
                                except:
                                    pass

                            raritybackground = Image.open(f'rarities/cataba/{rarity}.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
                            background = Image.open(f'rarities/cataba/{rarity}_background.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")

                            img=Image.new("RGB",(512,512))
                            img.paste(raritybackground)
                            try:
                                overlay = Image.open(f'rarities/cataba/{rarity}_overlay.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
                            except:
                                overlay = Image.open(f'rarities/cataba/common_overlay.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
                            img.paste(overlay, (0,0), overlay)
                            iconImg= Image.open(f'cache/{id}temp.png').resize((512, 512), Image.ANTIALIAS).convert('RGBA')
                            img.paste(iconImg, (0,0), iconImg)
                            img.paste(background, (0,0), background)
                            try:
                                rarityoverlay = Image.open(f'rarities/cataba/{rarity}_rarity.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
                            except:
                                rarityoverlay = Image.open(f'rarities/cataba/placeholder_rarity.png').resize((512, 512), Image.ANTIALIAS).convert("RGBA")
                            img.paste(rarityoverlay, (0,0), rarityoverlay)
                            img.save(f'cache/{id}.png')
                            loadFont = 'fonts/BurbankBigRegular-BlackItalic.otf'
                            font=ImageFont.truetype(loadFont,31)

                            background = Image.open(f'cache/{id}.png')
                            name=name.upper()
                            draw=ImageDraw.Draw(background)
                            draw.text((256,472),name,font=font,fill='white', anchor='ms') # Writes name

                            description=description.upper()
                            font=ImageFont.truetype(loadFont,10)
                            draw=ImageDraw.Draw(background)
                            draw.text((256,501),description,font=font,fill='white', anchor='ms') # Writes description

                            font=ImageFont.truetype(loadFont,14)
                            draw=ImageDraw.Draw(background)
                            draw.text((6,495),backendtype,font=font,fill='white') # Writes backend type        

                            background.save(f'icons/{id}.png')
                            os.remove(f'cache/{id}temp.png')
                            os.remove(f'cache/{id}.png')
                            counter = counter + 1
                            i = response.json()['items']
                            percentage = counter/len(i)
                            realpercentage = percentage * 100
                            print(f"{counter}/{len(i)} - {round(realpercentage)}%")

                        merger(mergewatermark)
                        # Merge is done, now tweeting 
                        import math

                        cap = f'Pak {pak} has been decrypted-\nFound {paknum} item(s) in Pak {pak}!\n\n#Fortnite'
                        try:
                            api.update_with_media("merged/merge.jpg",cap)
                        except:
                            foo = Image.open("merged/merge.jpg")
                            x, y = foo.size
                            x2, y2 = math.floor(x/2), math.floor(y/2)
                            foo = foo.resize((x2,y2),Image.ANTIALIAS)
                            foo.save("merged/merge.jpg",quality=65)
                            print('Compressed image!')
                            api.update_with_media("merged/merge.jpg",cap)
                        print('finished')

                        return test()



        else:
            print("FAILED TO GRAB NEWS DATA: URL DOWN")

        time.sleep(delay)

test()

