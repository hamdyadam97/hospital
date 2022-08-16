from django.db import models
from django.utils.translation.template import blankout

from patient.models import Patient
from account.models import Doctor


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    hour = models.CharField(max_length=20, blank=True, null=True)
    day = models.CharField(max_length=20, blank=True, null=True)
    date_appointment = models.DateField(blank=True, null=True)
    done = models.BooleanField(blank=True, null=False, default=False)

    def __str__(self):
        return format(self.doctor)


class Rate(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    rate = models.CharField(blank=True, null=True, max_length=20)
    notes = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return format(self.doctor)





