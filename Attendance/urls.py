from django.urls import path
from Attendance import views

urlpatterns = [
    path("",views.home),
    # path("/<str:date>/<str:section>", views.product, name='product'),
]
