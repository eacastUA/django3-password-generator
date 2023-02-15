from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')
def about(request):
    return render(request,'generator/about.html')
def password(request):
    
    
    characters = list('abcdefghijklmnopqrstuvwxyz')
    thePassword = ''
    upperList = []
    # print(characters)
    if request.GET.get('uppercase'):
        upperList = [x.upper() for x in characters]
        # print(upperList)
        # print(characters)
        characters += upperList
        # print(characters)
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+-=~'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    length = int(request.GET.get('length', 12))
    
    for x in range(length):
        thePassword += random.choice(characters)

    print(characters)
    return render(request,'generator/password.html', {'password' : thePassword})
        #  render(type, template, dictionary passed to template)