from django.urls import path
from Attendance import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("",views.home,name="attendance"),
    path("view/<str:_class>/<str:section>",views.view,name="attendance"),
    path("mark/<str:_class>/<str:section>",views.mark,name="attendance"),
    path("edit/<str:_class>/<str:section>",views.edit,name="attendance"),
    # path("/<str:date>/<str:section>", views.product, name='product'),
]
