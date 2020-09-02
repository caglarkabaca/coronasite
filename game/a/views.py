from django.shortcuts import render
from django.template import loader

# Create your views here.

from django.http import HttpResponse

def index(request):

    import json
    import random

    from django.templatetags.static import static

    with open(static('data.json')[1:], 'r') as f:

        data = json.loads(f.read())

    country_one = random.choice(data)
    #data.remove(country_one)
    country_two = random.choice(data)

    score = '0'

    if request.session.get('score', False):

        score = request.session['score']

    count_one = int(country_one[2].replace(',',''))
    count_two = int(country_two[2].replace(',',''))
    
    template = loader.get_template('a/index.html')
    context = {
        'u1_img' : country_one[3],
        'u1_name' : country_one[1],
        'u1_count' : country_one[2],
        'u2_img' : country_two[3],
        'u2_name' : country_two[1],
        'u2_count' : country_two[2],
        'score' : score,
        'u1_count_int' : count_one,
        'u2_count_int' : count_two,
    }

    return HttpResponse(template.render(context, request))

def add(request):

    from django.shortcuts import redirect

    if request.GET.get('lose', False):

        if request.session.get('score'):
            del request.session['score']
        return redirect('../')

    request.session['score'] = str(int(request.GET['score']) + 1)

    return redirect('../')