from django.shortcuts import render
from django.conf import settings
import requests
from products.models import *

def home(request):
    counters = [
        {'id':1,'finalCount':100,'duration':5000,'suffix':"%",'noteAbove':"","noteBelow":"Customer Satisfaction"},
        {'id':2,'finalCount':1,'duration':5000,'suffix':"%",'noteAbove':'lessThan','noteBelow':'Remake'},
        {'id':3,'finalCount':100,'duration':5000,'suffix':"%",'noteAbove':"",'noteBelow':'Digital Workflow'}
    ]
    reviews = [{'id':1},{'id':2},{'id':3},{'id':4},{'id':5}]
    review = Review.objects.all().order_by('-id')
    faqData = [
        {'id':1,"title":"Incoming Case Review","description":"Every incoming case is thoroughly reviewed for completeness and accuracy before proceeding to the design and fabrication stage."},
        {'id':2,"title":"CAD/CAM Design Fabrication","description":"Using advanced CAD/CAM systems, we craft precise restorations tailored to clinical specifications with exceptional materials and expert craftsmanship."},
        {'id':3,"title":"Precision Quality Check","description":'Each restoration undergoes a multi-step quality assurance process to ensure optimal fit, function, and aesthetics before final approval.'},
        {'id':4,"title":"Reliable Case Delivery","description":"Completed cases are securely packaged and dispatched on time, ensuring dependable delivery and consistent turnaround for your dental practice."}
    ]
    context = { 
        'counters':counters,
        'review':reviews,
        "faqdata":faqData
    }
    return render(request,'index.html',context)
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

def singleproduct(request,slug):
    # product = get_object_or_404(Product,slug=slug)
    # print("product",product)
    return render(request,'singleproduct.html')