from django.shortcuts import render

def index(request):
    return render(request, 'home.html', {})

def Login(request):
    return render(request,'usuarios/login.html')

