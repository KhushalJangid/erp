from django.urls import path
from Attendance import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("",views.home),
    path("view/<str:_class>/<str:section>",views.view),
    path("mark/<str:_class>/<str:section>",views.mark),
    path("edit/<str:_class>/<str:section>",views.edit),
    # path("/<str:date>/<str:section>", views.product, name='product'),
]
