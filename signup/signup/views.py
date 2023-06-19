from django.http import HttpResponse
from django.shortcuts import render

def login(request):
    # return HttpResponse('/home/hp/Downloads/signup/signup/login.html')
    return render (request,"login.html")

def home(request):
    return render(request,"home.html")

def signup(request):
    return render(request,"signup.html")

# Create your views here.
