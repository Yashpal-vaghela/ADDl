from django.urls import path,include
from . import views

app_name='home'

urlpatterns = [
    path('',views.home,name="home"),
    path('about-us',views.about,name="about"),
    path('contact-us',views.contact,name="contact"),
    path('support',views.support,name="support"),
    path('material',views.material,name="material"),
    path('products',views.product,name="product"),
    path('product/<slug:slug>',views.singleproduct,name="singleproduct")
]