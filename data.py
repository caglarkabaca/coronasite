def ref_data():

    URL = 'https://www.worldometers.info/coronavirus/#countries'

    RE = '<a class="mt_a" href="country/(.*)/">(.*)</a></td>\n<td style="font-weight: bold; text-align:right">(.*)</td>'


    from urllib.request import Request, urlopen

    import re

    req = Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read().decode('utf8')

    result = re.findall(RE, html)

    img_list = []

    tam_liste = []

    for index, ent in enumerate(result):

        n_tuple = (ent[0], ent[1], ent[2], 'img/' + ent[0])

        tam_liste.append(n_tuple)

    import json

    j_list = json.dumps(tam_liste)

    with open('data.json', 'w') as f:

        f.write(j_list)
    

