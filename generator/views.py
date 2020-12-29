from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):
    thepassword = ''
    caracteres = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length'))
    if request.GET.get('uppercase'):
        caracteres.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        caracteres.extend(list('0123456789'))
    if request.GET.get('special'):
        caracteres.extend(list('!@#$%^&*(-=+)'))
    for x in range(length):
        thepassword += random.choice(caracteres)
    return render(request, 'generator/password.html', {'password':thepassword})
