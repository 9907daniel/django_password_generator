from django.shortcuts import render
from django.http import HttpResponse

import random

# Create your views here.

def index(request):
    return render(request, 'generator_app/index.html', {'example' : 'This is curly bracket example'})


def about(request):
    return render(request, 'generator_app/about.html', {'aboutMe' : 'This is a about me syntax from views.py'})

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        #If checkbox 'uppercase' is selected, CAPS will be extended (appended) to the characters list

    if request.GET.get('specialChar'):
        characters.extend(list('!@#$%^&'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    length = int(request.GET.get('length'))

    thePassword = ''

    for x in range(length):
        thePassword += random.choice(characters)


    return render(request, 'generator_app/password.html', {'Password' : thePassword})


