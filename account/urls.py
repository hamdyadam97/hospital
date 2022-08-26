from .views import *
from django.urls import path
urlpatterns = [
    path('signup/', RegisterUserAPIView.as_view(), name='signup'),
    path('signin/', UserLoginView.as_view(), name='signin'),
    path('createprofiledoctor/', doctorprofile, name='createprofiledoctor'),
    path('doctordata/<username>', get_doctor_data, name='get_doctor_data'),
    path('api/', doctor_view, name='doctor_view'),
    path('updateprofile/', update_profile_doctor, name='updateprofile'),
    path('sendnumbertoverify/<username>', create_verify_num, name='sendnumbertoverify'),
    path('numbertoverify/<username>', verify_num, name='numbertoverify'),
]