from django.urls import path
from .views import *
urlpatterns=[
        path("",home,name="course-home"),
        path("new/",NewCourse.as_view(),name='course-new'),
]