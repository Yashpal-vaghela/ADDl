import requests
from django.shortcuts import redirect, render
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm, ChatEnquiryForm

def contactd(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.RECAPTCHA_SECRET_KEY,  
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        if not result.get('success'):
            messages.error(request, 'Invalid reCAPTCHA. Please try again.')
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        if form.is_valid():
            form.save()   # ✅ only save in database (admin panel)
            messages.success(request, 'Thank you! We’ll reach you soon.')
        else:
            messages.error(request, 'Please Try Again')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
    context = {
        "RECAPTCHA_SITE_KEY": settings.RECAPTCHA_SITE_KEY
    }
    return render(request, 'contact.html', context)

def save_chat_enquiry(request):
    if request.method == "POST":
        form = ChatEnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! We’ll reach you soon.')
        else:
            messages.error(request, 'Please Try Again')
        return redirect(request.META.get('HTTP_REFERER', '/'))