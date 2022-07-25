from django.urls import path
from Accounts import views

urlpatterns = [
    path('',views.home),
    path('login', views.login_user),
    path('add_student', views.add_student),
    path('add_faculty', views.add_faculty),
    
]
