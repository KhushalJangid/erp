from django.test import TestCase
from .models import Faculty,Student,User
from Attendance.models import ClassesCollection
from json import dumps
# Create your tests here.

def setr():
    query = Student.objects.all()
    for q in query:
        f_name = q.user.first_name
        l_name = q.user.last_name
        username = q.user.username
        ClassesCollection(f"12_A").addStudent(username=username,name=f"{f_name} {l_name}")
    return