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
    return render(request,"login.html")

# @method_decorator(login_required,name='get')
class Faculty(View):
    def get(self,**kwargs):
        _class = kwargs["class"]
        _date = parseGet(self.request,"date")
        if _date == "":
            _from = parseGet(self.request,"from")
            _to = parseGet(self.request,"to")
            table = Collection(_class)
            obj = table.filter(_from,_to)
            print(obj)
            return
        else :
            table = Collection(_class)
            obj = table.get(date=_date)
            print(obj)
            return
    def post(request,**kwargs):
        _class = kwargs["class"]
    
class Admin(View):
    def get(self,request):
        return