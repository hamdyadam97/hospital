from django.urls import path
from .views import *
app_name = 'appointment'
urlpatterns = [
    path('rate/<doctor>', rate, name='rate'),
    path('appointment/', make_appointment, name='appointment'),
    path('history/<patient>', history_of_patient, name='history'),
    path('delete/<id>', cancel_appointment, name='history'),
    path('cancel_appointment/<id>', send_note, name='send_note'),
    path('historyofdoctor/<username>', history_of_doctor, name='historyofdoctor'),
    path('done_appointment/<id>', make_appointment_done, name='historyofdoctor'),
]
 