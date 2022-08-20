from django.contrib.auth.models import User
from django.db import models
choice = (
    ('female', 'female'),
    ('male', 'male'),
)


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_query_name='pat')
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(blank=True, null=True, max_length=20, choices=choice)
    history = models.TextField(max_length=200, blank=True, null=True)
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to='patient', default='E:/GP/media/profile/l.jpg', blank=True, null=True)

    def __str__(self):
        return format(self.user)

    def save(self, *args, **kwargs):
        try:
            if self.user.doc:
                return
        except:
            super(Patient, self).save(*args, **kwargs)
