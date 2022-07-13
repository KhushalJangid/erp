from django.shortcuts import render
from datetime import datetime
# Create your views here.

def home(request):
    return render(request,"login.html")

def add(request,section):
    if request.method == "POST":
        pass
    return