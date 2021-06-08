from django.urls import path
from .views import *

urlpatterns = [
    path("user_list/", UserList.as_view()),
    path("signup/", signup),
    path("admin_signup/", admin_signup),
    ]
