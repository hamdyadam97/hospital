import datetime
from urllib import request
from django.conf import settings
from django.core.checks import messages
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify
from rest_framework.authtoken.models import Token
from patient.models import Patient
from dateutil.relativedelta import relativedelta
Day = (
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
)
choice = (
    ('female', 'female'),
    ('male', 'male'),
)
DOCTOR_IN = (
    ('leather', 'leather'),
    ('teeth', 'teeth'),
    ('psychiatrist', 'psychiatrist'),
    ('newborn children', 'newborn children'),
    ('brain and nerves', 'brain and nerve'),
    ('bones', 'bones'),
    ('Obstetrician and gynecologist', 'Obstetrician and gynecologist'),
    ('ear, nose and throat', 'ear, nose and throat'),
    ('Heart and blood vessels', 'Heart and blood vessels'),
    ('blood diseases', 'blood diseases'),
    ('oncologist', 'oncologist'),
    ('inner', 'internal'),
    ('Slimming and Nutrition', 'Slimming and Nutrition'),
    ('pediatric surgery', 'pediatric surgery'),
    ('Oncology', 'Oncology'),
    ('plastic surgery', 'cosmetic surgery'),
)


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='doc')
    bio = models.TextField("bio",max_length=500, blank=True)
    address = models.CharField("country ", max_length=100, blank=True, null=True)
    address_detail = models.CharField("address_detail", max_length=100, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(choices=choice, blank=True,max_length=10)
    doctor = models.CharField("doctor", max_length=100, choices=DOCTOR_IN, blank=True, null=True)
    specialist_doctor = models.CharField("  specialist_doctor", max_length=100, blank=True, null=True)
    price = models.IntegerField(" price", blank=True, null=True)
    from_of_work = models.IntegerField("from_of_work", blank=True, null=True)
    to_of_work = models.IntegerField("to_of_work", blank=True, null=True)
    day1_of_work = models.CharField("day1_of_work", choices=Day, blank=True, null=True,max_length=20)
    day2_of_work = models.CharField("day2_of_work", choices=Day, blank=True, null=True,max_length=20)
    day3_of_work = models.CharField("day3_of_work", choices=Day, blank=True, null=True,max_length=20)
    mobile = models.CharField(" mobile", blank=True, null=True,max_length=11)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    google = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    avg = models.CharField(max_length=20,null=True, blank=True,default='no hava rate yet')
    image = models.ImageField(" image", upload_to="profile", default="E:/GP/media/profile/l.jpg", null=True, blank=True)
    slug = models.SlugField("slug", blank=True, null=True)

    def save(self, *args, **kwargs):
        patient = Patient.objects.filter(user=self.user)
        if patient:
            return
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Doctor, self).save(*args, **kwargs)

    def __str__(self):
        return format(self.user)


class ISActive(models.Model):
    user_active = models.OneToOneField(User,on_delete=models.CASCADE,related_name='active_user')
    is_active = models.BooleanField("is_active", blank=True, null=False, default=False)
    num_verify = models.IntegerField("num_verify", blank=True, null=True)
    created_date = models.DateTimeField(auto_now=True)
    expire_date = models.DateTimeField(null=True, blank=True)

    def save(self,*args, **kwargs):
        self.expire_date = datetime.datetime.now(datetime.timezone.utc) + relativedelta(minutes=5)
        print((self.expire_date))
        super(ISActive, self).save(*args, **kwargs)

    def __str__(self):
        return format(self.user_active)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)




# @receiver(post_save, sender=Patient)
# def create_doctor_patient(sender, instance, created, **kwargs):
#     if created:
#         doc = instance.user
#         rates = Doctor.objects.filter(user=doc)
#         if rates:
#             instance.delete()

# for user in User.objects.all():
#     Token.objects.get_or_create(user=user)