from django.urls import path
from . import views

app_name = 'enquiry'
urlpatterns = [
    path('contact-data/', views.contactd, name='contactd'),
    path('save-chat/', views.save_chat_enquiry, name="save_chat")
]
