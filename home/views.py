from django.shortcuts import render
from django.conf import settings
import requests

def home(request):
    return render(request,'index.html')
# Create your views here.

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request, 'contact.html', {
        "RECAPTCHA_SITE_KEY": settings.RECAPTCHA_SITE_KEY
    })

def support(request):
    return render(request,'support.html')

def material(request):
    return render(request,'material.html')

def product(request):
    return render(request,'product.html')