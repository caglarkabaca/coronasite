"""


<a class="mt_a" href="country/turkey/">Turkey</a></td>
<td style="font-weight: bold; text-align:right">270,133</td>

https://www.worldometers.info/coronavirus/#countries


<img src="/img/flags/small/tn_us-flag.gif" width="60" border="1 px solid #aaa">

<h1>
<div style="display:inline"> <img src="/img/flags/small/tn_br-flag.gif" width="60" border="1 px solid #aaa"></div>

"""

URL = 'https://www.worldometers.info/coronavirus/#countries'

RE = '<a class="mt_a" href="country/(.*)/">(.*)</a></td>\n<td style="font-weight: bold; text-align:right">(.*)</td>'


from urllib.request import Request, urlopen

import re

req = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req).read().decode('utf8')

result = re.findall(RE, html)

#with open('test.txt', 'w', encoding="utf-8") as f:
#
#   f.write(html)

img_list = []

tam_liste = []

for index, ent in enumerate(result):

    import os

    os.system('cls')
    print(f'{index + 1} / {len(result)}')

    f_new_url = 'https://www.worldometers.info/coronavirus/country/' + ent[0]

   

    #print(ent)

    f_re = '<div style="display:inline"> <img src="/img/flags/small/(.*?)" width="60" border="1 px solid #aaa" /></div>'

    f_req = Request(f_new_url, headers={'User-Agent': 'Mozilla/5.0'})
    f_html = urlopen(f_req).read().decode('utf8')

    f_result = re.findall(f_re, f_html)

    img_list.append('https://www.worldometers.info/img/flags/small/' + f_result[0])

    n_tuple = (ent[0], ent[1], ent[2], 'https://www.worldometers.info/img/flags/small/' + f_result[0])

    tam_liste.append(n_tuple)
    #with open('test1.txt', 'w', encoding='utf-8') as f:
    #
    #   f.write(f_html)

import json

j_list = json.dumps(tam_liste)

with open('data.json', 'w') as f:

    f.write(j_list)
    
