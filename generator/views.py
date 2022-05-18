from random import random
from django import http
from django.shortcuts import render

import generator
import random
#from django.http import HttpResponse, response

def about(request):
    return render(request,"about.html")

def home(request):
    return  render(request,"home.html")

    

def password(request):

    characteres = list("abcdefghijklmñopqrst")
    generated_password = ''

    length= int(request.GET.get('leng'))

    if request.GET.get('uppercase'):
        characteres.extend(list('ABCDEFGHIJKLMÑOPQRST'))
    if request.GET.get('special'):
        characteres.extend(list('¡?#$%&'))
    if request.GET.get('numbers'):
        characteres.extend(list('0123456789'))

    
    for x in range(length) : 
        generated_password+= random.choice(characteres)

    return render(request,"password.html", {'password' :generated_password})