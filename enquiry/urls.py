from django.urls import path
from . import views

app_name = 'enquiry'
urlpatterns = [
    path('contact-data/', views.contactd, name='contactd'),
]
