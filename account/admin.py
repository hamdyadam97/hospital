from django.contrib import admin
from django.core.checks import messages

from account.models import Doctor

admin.site.register(Doctor)


# def save_model(self, request, obj, form, change):
#     messages.set_level(request, messages.ERROR)
#     messages.error(request, 'No changes are permitted ..')