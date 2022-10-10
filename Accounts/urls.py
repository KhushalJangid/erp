from django.urls import path,re_path
from Accounts import views

urlpatterns = [
    path('',views.home),
    re_path(r'login/?$', views.login_user),
    re_path(r'add_student/?$', views.add_student),
    re_path(r'add_faculty/?$', views.add_faculty),
    
]
