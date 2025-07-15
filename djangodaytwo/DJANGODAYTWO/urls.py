from django.contrib import admin
from django.urls import path, include
from DJANGODAYTWO import views

urlpatterns = [
    path('home/', views.home),
    path('about/', views.about),
    path('home/', views.home),
    path('home/', views.home),
    path('home/', views.home),
]