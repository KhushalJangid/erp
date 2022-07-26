from django.test import TestCase
from .models import Faculty,User
from json import dumps
# Create your tests here.

def setr():
    user = User.objects.get(username=484298)
    obj = Faculty.objects.get(user = user)
    obj.classes = dumps(["12_a"])
    obj.save()
    print(obj)