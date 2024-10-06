# from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse('Hello, Home page!')
    return render(request, 'home.html')

def about(request):
    # return HttpResponse('About us')
    return render(request, 'about.html')
