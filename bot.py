import requests
import os
import time

print('Starting the fishey bot OwO UwU')

#------

headers = {'Authorization': 'b8f04d76-413b547e-15425588-111d0274'}

#------

apiurl = 'https://fortniteapi.io/v1/loot/fish?lang=en'

try:    
    response = requests.get('https://fortniteapi.io/v1/loot/fish?lang=en', headers=headers)
    # this is to see if the api is up or not - means nothing dont ask bruh
    result = response.json()['result']
    print('Grabbed the API succesfully.')
except:
    print('\nAPI is down or there was an error. Closing program.\n')
    exit()

f= open(f'allfish.txt', 'w')

print('\nDo you want to grab the list of all fish or fish stats? - all/stats')
ask = input()

if(ask == 'all'):
    print('\nGrabbing fish info...')
    for item in response.json()["fish"]:
        name = item["name"]
        desc = item['description']
        rarity = item['rarity']
        f.write(f'{name} - {rarity}\n{desc}\n\n')
	    print(f'\nGrabbed the {name} fish')

if(ask == "stats"):
    print('\nWhat user do you want to grab fish stats from?')
    name = input()
    response = requests.get(f'https://fortnite-api.com/v1/stats/br/v2?name={name}')
    accountid = response.json()['data']['account']['id']
    print('\nWhich season do you want to grab stats from? - 14/15')
    season = input()
    if(season == '14'):
	    fishapi = requests.get(f'https://fortniteapi.io/v1/stats/fish?accountId={accountid}', headers=headers)
	    fishstats = fishapi.json()['stats'][0]['fish']
	    for fish in fishapi:
		    name = fish['name']
		    print(f'{name}\n')

    x = len(fishapi)

print('\nDone!')

f.close()
