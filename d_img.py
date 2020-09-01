import json
import requests

def dw_img(data):

    resp = requests.get(data[3])

    with open('img/' + data[0] + '.gif', 'wb') as f:

        f.write(resp.content)
    

STR = ''

with open('data.json', 'r') as file:

    STR = file.read()

big_data = json.loads(STR)

import os

for index, data in enumerate(big_data):

    os.system('cls')
    print(f' { index + 1} / { len(big_data) }')

    dw_img(data)