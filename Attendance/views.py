from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from django.views import View
from .models import Collection
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
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
        return render(request,"attendance/attendance_teacher.html")
    else:
        pass
    return render(request,"login.html")

# @method_decorator(login_required,name='get')
class Faculty(View):
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