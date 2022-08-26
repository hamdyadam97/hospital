from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.core.checks import messages
from account.models import Doctor, ISActive
from patient.admin import RateInlineAdmin, AppointmentInlineAdmin

admin.site.unregister(Group)


class ISActiveAdmin(admin.ModelAdmin):
    list_display = ['user_active', 'is_active', 'expire_date']


class DoctorAdmin(admin.ModelAdmin):
    list_display = ['user', 'doctor', 'address', 'price', 'specialist_doctor', 'avg', 'day_of_work']
    list_editable = ['price','address']
    list_filter = ('doctor',)
    inlines = [RateInlineAdmin, AppointmentInlineAdmin]

    def day_of_work(self, obj):
        return f'day that doctor available {obj.user}  '"{}{}{}".format(obj.day1_of_work, obj.day2_of_work,
                                                                        obj.day3_of_work)


admin.site.register(ISActive, ISActiveAdmin)
admin.site.register(Doctor, DoctorAdmin)