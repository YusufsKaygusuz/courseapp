from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
'''
path('', views.home),
    path('mainpage', views.home),
    path('contact', views.contact),
    path('about', views.contact)
'''

def index(request):
    return render(request, 'pages/index.html')

def contact(request):
    return render(request, 'pages/contact.html')

def about(request):
    return render(request, 'pages/about.html')