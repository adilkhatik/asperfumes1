from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name='home'),
    path('about',views.about,name='about'),
    path('services',views.services,name='services'),
    path('contact',views.contact,name='contact'),
    path('Normal_Attar',views.Normal_Attar,name='Normal Attar'),
    path('Special_Attar',views.Special_Attar,name='Special Attar'),
    path('Premium_Attar',views.Premium_Attar,name='Premium Attar'),
    path('Normal_Perfumes',views.Normal_Perfumes,name='Normal Perfumes'),
    path('Special_Perfumes',views.Special_Perfumes,name='Special Perfumes'),
    path('Customizations',views.Customizations,name='Customizations'),


]
