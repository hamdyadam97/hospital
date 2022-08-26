from django.contrib import admin
from .models import Appointment, Rate, Notification


class NotificationInlineAdmin(admin.StackedInline):
    model = Notification
    extra = 1


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'patient', 'hour', 'day', 'date_appointment', 'explain_of_appointment', ]
    list_filter = ['doctor', 'patient', 'hour', 'day', 'date_appointment']
    list_editable = ['hour', 'day', 'date_appointment']
    inlines = [NotificationInlineAdmin]

    def explain_of_appointment(self, obj):
        return "{} has appointment with doctor {} in {}".format(obj.patient, obj.doctor, obj.date_appointment)


class RateAdmin(admin.ModelAdmin):
    list_display = ['doctor', 'patient', 'rate', 'notes']


class NotificationAdmin(admin.ModelAdmin):
    list_display = ['app', 'owner', 'read', 'msg']


admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Rate, RateAdmin)
admin.site.register(Notification, NotificationAdmin)