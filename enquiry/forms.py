from django import forms
from .models import Contact, ChatEnquiry

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
class ChatEnquiryForm(forms.ModelForm):
    class Meta:
        model = ChatEnquiry
        fields = ['name', 'email']