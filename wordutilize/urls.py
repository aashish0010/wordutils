from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.word, name='home'),
    path('analize', views.analize, name='analize'),
 ]
