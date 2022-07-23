from django.urls import path
from Attendance import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("/faculty/<str:class>",login_required(views.Faculty.as_view())),
    # path("/<str:date>/<str:section>", views.product, name='product'),
]
