from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.views import View
from .models import Collection
from Accounts.models import Faculty, User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from json import dumps,loads
from Accounts.tests import setr
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
            table = Collection(_class)
            obj = table.get(date=datetime.now().strftime("%d-%m-%Y"))
            status = True if obj else False
            if status :
                att = obj["attendance"]
                att = list(att.values())
                total = len(att)
                present = att.count(1)
                absent = total - present
                c = _class.split("_")
                dic[_class] = {"status":status,
                               "class" : c[0],
                               "section": c[-1].upper(),
                                "total": total,
                                "present": present,
                                "absent": absent,
                                }
            else :
                c = _class.split("_")
                dic[_class] = {"status":status,
                               "class" : c[0],
                               "section": c[-1].upper(),
                               }
        context["data"] = dic
        return render(request,"attendance/attendance_teacher.html",context=context)
    else:
        pass
    return render(request,"login.html")

# @method_decorator(login_required,name='get')
class FacultyView(View):
    '''CBV for Searching/Adding/Editing attendance by faculty'''
    def get(self,request,**kwargs):
        if request.user.is_staff:
            _class = kwargs["class"]
            section = kwargs["section"]
            table = Collection(f"{_class}_{section}")
            _date = parseGet(self.request,"date")
            if _date == "":
                _from = parseGet(self.request,"from")
                if _from == "":
                    obj = table.get(date=datetime.now().strftime("%d-%m-%Y"))
                    data = obj["attendace"]
                    return HttpResponse(data)
                _to = parseGet(self.request,"to")
                obj = table.filter(_from,_to)
                print(obj)
                return
            else :
                obj = table.get(date=_date)
                print(obj)
                return
        return HttpResponse(content="You are not authorized !",status=403)
    
    def post(self,request,**kwargs):
        if request.user.is_staff:
            _class = kwargs["class"]
            section = kwargs["section"]
        return HttpResponse(content="You are not authorized !",status=403)
class Admin(View):
    '''CBV for Searching/Adding/Editing attendance by site admin'''
    def get(self,request):
        return