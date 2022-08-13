from django.urls import path
from .views import *
app_name = 'appointment'
urlpatterns = [
    path('rate/<doctor>', rate, name='rate'),
    path('appointment/', make_appointment, name='appointment'),
    path('history/<patient>', history_of_patient, name='history'),
    path('delete/<id>', cancel_appointment, name='history'),
]
 