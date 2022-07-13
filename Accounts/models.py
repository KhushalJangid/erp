from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

_posts = [("st","Student"),
          ("fc","Faculty"),
          ("ad","Admin")]

_genders = [("m","Male"),
           ("f","Female"),
           ("o","Others")]

_bg = [("a","A"),
       ("b","B"),
       ("o","O")]

_year = [
    (1,"First"),
    (2,"Second"),
    (3,"Third"),
    (4,"Fourth"),
]
class User(AbstractUser):
    # id = models.BigAutoField(primary_key=True)
    # first_name
    middle_name = models.CharField(null=True,blank=True,max_length=15)
    # last_name
    # username
    avatar = models.ImageField(upload_to='avatars/',default='avatars/profile-user.png')
    gender = models.CharField(max_length=10,choices=_genders)
    email = models.EmailField(blank=True,null=True,unique=False)
    phone = models.CharField(blank=True,null=True,unique=True,max_length=15)
    dob = models.DateField()
    address = models.TextField(blank=True,null=True,max_length=200)
    aadharno = models.IntegerField(unique=True,null=True,blank=True)
    post = models.CharField(max_length=10,choices=_posts)
    # username = models.CharField(max_length=15,unique=True)

    objects = UserManager()

class Student(models.Model):
    user = models.OneToOneField(to = User,on_delete=models.CASCADE)
    # ? Academic Details
    admNumber = models.CharField(max_length=15)
    enrollNumber = models.IntegerField()
    rollno = models.CharField(null=True,unique=True,max_length=15)
    specialization = models.CharField(max_length = 20)
    year = models.IntegerField()
    sem = models.IntegerField()
    section = models.CharField(max_length=2)
    passout = models.IntegerField()
    #? Personal Details
    bloodGroup = models.CharField(max_length=3,choices=_bg)


class Teacher(models.Model):
    user = models.OneToOneField(to = User,on_delete=models.CASCADE)
    specialization = models.CharField(max_length = 20)

class Sections(models.Model):
    faculty = models.ForeignKey(to=Teacher,on_delete=models.CASCADE)
    year = models.IntegerField(choices=_year)
    name = models.CharField(max_length=2)