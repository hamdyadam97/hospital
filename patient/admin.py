from django.contrib import admin
from django.contrib.auth.models import User

from appointment.models import Appointment, Rate
from patient.models import Patient


class AppointmentInlineAdmin(admin.StackedInline):
    model = Appointment
    # extra = 1


class RateInlineAdmin(admin.StackedInline):
    model = Rate
    # extra = 1


class PatientAdmin(admin.ModelAdmin):
    list_display = ['user', 'age', 'gender', 'mobile', 'history', 'show_some_detail']
    list_editable = ['mobile', 'history']
    list_select_related = ['user']
    list_filter = ['gender']
    inlines = [AppointmentInlineAdmin, RateInlineAdmin]

    def show_some_detail(self, obj):
        return "age of {} is {} that may have some common of {}".format(obj.user, obj.age, obj.history)


admin.site.register(Patient, PatientAdmin)

