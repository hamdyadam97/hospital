from .views import *
from django.urls import path
urlpatterns = [
    path('signup/', RegisterUserAPIView.as_view(), name='signup'),
    path('signin/', UserLoginView.as_view(), name='signin'),
    path('createprofiledoctor/', doctorprofile, name='createprofiledoctor'),
]