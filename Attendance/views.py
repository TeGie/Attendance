from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'attendance/home.html')

def login(request):
    return render(request, 'attendance/login.html')
