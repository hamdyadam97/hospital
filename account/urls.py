from .views import *
from django.urls import path
urlpatterns = [
    path('signup/', RegisterUserAPIView.as_view(), name='signup'),
]