from .views import *
from django.urls import path
app_name = 'patient'
urlpatterns = [
    path('createpateintprofile', patient_profile, name='createpateintprofile'),
    path('patientdata/<username>', get_patient_data, name='get_patient_data'),

]