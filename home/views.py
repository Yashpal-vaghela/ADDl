from django.shortcuts import render
from django.conf import settings
import requests

def home(request):
    return render(request,'index.html')
# Create your views here.
