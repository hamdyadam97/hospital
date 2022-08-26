from attr.validators import max_len
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from account.models import Doctor
from patient.models import Patient


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,related_name='doc')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,related_name='pat')
    hour = models.CharField(max_length=20, blank=True, null=True)
    day = models.CharField(max_length=20, blank=True, null=True)
    date_appointment = models.DateField(blank=True, null=True)
    done = models.BooleanField(blank=True, null=False, default=False)
    cancel = models.BooleanField(blank=True,null=False,default=False)

    def __str__(self):
        return format(self.doctor)


class Rate(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    rate = models.CharField(blank=True, null=True, max_length=20)
    notes = models.TextField(max_length=500, blank=True, null=True)

    def __str__(self):
        return format(self.doctor)


@receiver(post_save, sender=Rate)
def create_rate_doctor(sender, instance, created, **kwargs):
    if created:
        doc = instance.doctor
        rates = Rate.objects.filter(doctor=doc)
        the_count_of_rate = rates.count()
        total = 0
        for i in rates:
            total += int(i.rate)
            avg = total / the_count_of_rate
        Doctor.objects.filter(id=doc.id).update(avg=avg)


class Notification(models.Model):
    app = models.ForeignKey(Appointment, on_delete=models.CASCADE,related_name='app')
    read = models.BooleanField(blank=True, null=False, default=False)
    msg = models.TextField(blank=True, null=True)
    owner = models.CharField(blank=True, null=True, max_length=20)

    def __str__(self):
        return format(self.app)


@receiver(post_save, sender=Appointment)
def create_notification_appointment(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(app=instance, msg=f'appointment created by patient {instance.patient}',owner=instance.doctor)
