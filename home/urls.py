from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('home', views.home, name='Home'),
    
    path('about', views.about, name='About'),
    path('contact', views.contact, name='Contact'),
    path('AI', views.ai, name='AI'),
    path('DataScience', views.dataScience, name='Data Science'),
    path('MachineLearning', views.machineLearning, name='Machine Learning'),




]