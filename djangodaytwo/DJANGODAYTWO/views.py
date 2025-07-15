from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Welcome to the home page of DJANGODAYTWO!")
def about(request):
    return HttpResponse("This is the about page of DJANGODAYTWO!")  
def contact(request):           
    return HttpResponse("This is the contact page of DJANGODAYTWO!")
def services(request):
    return HttpResponse("These are the services offered by DJANGODAYTWO!")
