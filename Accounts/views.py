from django.http import HttpResponse
from django.shortcuts import render

from .models import User

# Create your views here.
def loginUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        return HttpResponse("Accepted")

    else:
        return render(request, "login.html")

