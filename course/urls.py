from django.urls import path
from .views import *
urlpatterns=[
        path("new/",home,name="course-home")
]