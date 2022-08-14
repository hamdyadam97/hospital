from .views import *
from django.urls import path
app_name = 'patient'
urlpatterns = [
    path('createpateintprofile', pateintprofile, name='createpateintprofile'),
    path('patientdata/<username>', get_patient_data, name='get_patient_data'),

]