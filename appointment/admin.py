from django.contrib import admin
from .models import Appointment, Rate,Notification


admin.site.register(Rate)
admin.site.register(Notification)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['id','doctor','patient']

admin.site.register(Appointment,AppointmentAdmin)