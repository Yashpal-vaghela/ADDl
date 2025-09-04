from django.shortcuts import redirect
from django.contrib import messages
from .forms import ContactForm

def contactd(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()   # ✅ only save in database (admin panel)
            messages.success(request, 'Thank you! We are reaching you soon.')
        else:
            messages.error(request, 'Please Try Again')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
