from django.urls import path
from Accounts.views import loginUser

urlpatterns = [
    path('', loginUser),
    
]
