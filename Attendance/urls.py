from django.urls import path
from Attendance import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("",views.home),
    path("faculty/<str:class>/<str:section>",login_required(views.FacultyView.as_view())),
    # path("/<str:date>/<str:section>", views.product, name='product'),
]
