from django.http import HttpResponse
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import redirect, render
from datetime import datetime
from .models import Faculty, Student, User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    if request.user.post == "ad":
        return render(request,"dashboard_teacher.html")
    elif request.user.post == "fc":
        return render(request,"dashboard_teacher.html")
    else:
        return render(request,"dashboard_teacher.html")

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            route = request.GET.get("next")
            if route:
                return redirect(route)
            return redirect("/")
        else:
            return HttpResponse(content="Invalid credentials",status=403)
        
    return render(request,"accounts/login_form.html")

@login_required
def add_student(request):
    if request.user.is_staff:
        if request.method == "POST":
            # print(request.POST)
            # username = 
            name = request.POST.get("name")
            _class = request.POST.get("class")
            section = request.POST.get("section")
            aadhar = request.POST.get("aadhar")
            name = name.split(" ")
            f_name = name[0]
            l_name = name[-1]
            user = User.objects.create(username=aadhar,
                                    first_name=f_name,
                                    last_name=l_name,
                                    #    aadharno=aadhar,
                                    post="st")
            st = Student.objects.create(
                user = user,
                _class=_class,
                section =section,
            )
            st.save()
            year = str(datetime.now())[:4]
            password = f"{f_name[:2]}@{year}"
            user.set_password(password)
            user.save()
            return redirect("/")
        return render(request,"accounts/add_student.html")
    else :
        return HttpResponse(content="You are not authorized !",status=403)

@login_required
def add_faculty(request):
    if request.user.post == "ad":
        if request.method == "POST":
            # print(request.POST)
            # username = 
            # _class = request.POST.get("class")
            aadhar = request.POST.get("aadhar")
            subject = request.POST.get("subject")
            f_name = request.POST.get("first_name")
            l_name = request.POST.get("last_name")
            user = User.objects.create(username=aadhar,
                                    first_name=f_name,
                                    last_name=l_name,
                                    #    aadharno=aadhar,
                                    is_staff=True,
                                    post="fc")
            fc = Faculty.objects.create(
                user = user,
                specialization = subject
                # _class=_class,
                # section =section,
            )
            fc.save()
            year = str(datetime.now())[:4]
            password = f"{f_name[:2]}@{year}"
            user.set_password(password)
            user.save()
            return redirect("/")
        return render(request,"accounts/add_faculty.html")
    else :
        return HttpResponse(content="You are not authorized !",status=403)
    
    