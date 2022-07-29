from re import A
from django.http import HttpResponse
from django.shortcuts import redirect, render
from datetime import datetime
from django.views import View
from .models import AttendanceCollection,ClassesCollection
from Accounts.models import Faculty, Student, User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from json import dumps,loads
from Accounts import serializers
from django.contrib import messages
# Create your views here.

def parseGet(request,kw):
    _ = request.query_params.get(kw)
    if _:
        return _
    else:
        return ""

@login_required()
def home(request):
    '''Attendance Home. serves page respective to the post of user.'''
    if request.user.post == "ad":
        pass
    elif request.user.post == "fc":
        context = {}
        dic = {}
        user = request.user
        data = Faculty.objects.get(user=user)
        meta = data.classes
        data = loads(meta)
        for _class in data:
            table = AttendanceCollection(_class)
            obj = table.get(date=datetime.now().strftime("%d-%m-%Y"))
            status = True if obj else False
            if status :
                att = obj["attendance"]
                # att = att.values()
                total = len(att)
                present = 0
                for value in att.values():
                    if value["status"] == "Present":
                        present+=1
                absent = total - present
                c = _class.split("_")
                dic[_class] = {"status":status,
                               "class" : c[0],
                               "section": c[-1],
                                "total": total,
                                "present": present,
                                "absent": absent,
                                }
            else :
                c = _class.split("_")
                st = serializers.get_student_list(_class=int(c[0]),section=c[-1]).keys()
                dic[_class] = {"status":status,
                               "class" : c[0],
                               "section": c[-1],
                               "total":len(list(st))
                               }
        context["data"] = dic
        return render(request,"attendance/attendance_teacher.html",context=context)
    else:
        '''handle student attendance view here 
        (filter by date through post request)'''
        if request.method == "POST":
            pass
        pass

@login_required()
def view(request,_class,section):
    if request.user.is_staff:
        if request.method == "GET":
            data = {}
            std = ClassesCollection(f"{_class}_{section}").get()
            table = AttendanceCollection(f"{_class}_{section}")
            obj = table.get(date=datetime.now().strftime("%d-%m-%Y"))
            att = obj["attendance"]
            students = std["students"]
            idx = 1
            for key, value in students.items():
                data[idx] = {
                    'uid':key,
                    'name':value,
                    'status':att[key]['status'],
                    'remarks':att[key]['remarks'],
                }
                idx+=1
            context = {
                "class":_class,
                "section":section,
                "data":data
                }
            return render(request,"attendance/view_attendance_teacher.html",context)

        
    return HttpResponse(content="You are not authorized !",status=403)

@login_required()
def mark(request,_class,section):
    if request.user.is_staff:
        if request.method == "GET":
            data = {}
            obj = ClassesCollection(f"{_class}_{section}").get()
            students = obj["students"]
            idx = 1
            for key, value in students.items():
                data[idx] = {
                    'uid':key,
                    'name':value
                }
                idx+=1
            context = {
                "class":_class,
                "section":section,
                "data":data
                }
            return render(request,"attendance/mark_attendance_teacher.html",context)
        elif request.method == "POST":
            data = {}
            obj = ClassesCollection(f"{_class}_{section}").get()
            students = obj["students"]
            for key, value in students.items():
                status = request.POST.get(f'{key}_status')
                remarks = request.POST.get(f'{key}_remarks')
                data[key] = {
                    'status':status,
                    'remarks':remarks,
                }
            ctx = {
                "date" : datetime.now().strftime("%d-%m-%Y"),
                "attendance":data,
            }
            table = AttendanceCollection(f"{_class}_{section}")
            table.insert(ctx)
            messages.info(request,f"Attendance for class {_class} {section} is saved !")
            return redirect("/attendance")
        else :
            return HttpResponse(content="Only GET & POST requests are allowed.",status=403)
    return HttpResponse(content="You are not authorized !",status=403)
    
@login_required()
def edit(request,_class,section):
    if request.user.is_staff:
        if request.method == "GET":
            data = {}
            std = ClassesCollection(f"{_class}_{section}").get()
            table = AttendanceCollection(f"{_class}_{section}")
            obj = table.get(date=datetime.now().strftime("%d-%m-%Y"))
            att = obj["attendance"]
            students = std["students"]
            idx = 1
            for key, value in students.items():
                data[idx] = {
                    'uid':key,
                    'name':value,
                    'status':att[key]['status'],
                    'remarks':att[key]['remarks'],
                }
                idx+=1
            context = {
                "class":_class,
                "section":section,
                "data":data
                }
            return render(request,"attendance/edit_attendance_teacher.html",context)
        elif request.method == "POST":
            data = {}
            obj = ClassesCollection(f"{_class}_{section}").get()
            students = obj["students"]
            for key, value in students.items():
                status = request.POST.get(f'{key}_status')
                remarks = request.POST.get(f'{key}_remarks')
                data[key] = {
                    'status':status,
                    'remarks':remarks,
                }
            table = AttendanceCollection(f"{_class}_{section}")
            # table.insert(ctx)
            table.update(date=datetime.now().strftime("%d-%m-%Y"),attendance=data)
            messages.info(request,f"Attendance for class {_class} {section} is saved !")
            return redirect("/attendance")
        else :
            return HttpResponse(content="Only GET & POST requests are allowed.",status=403)
    return HttpResponse(content="You are not authorized !",status=403)
    return render(request,"attendance/edit_attendance_teacher.html")
