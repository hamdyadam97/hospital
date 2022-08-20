from rest_framework import serializers
from appointment.models import Rate, Appointment, Notification


class DoctorRate(serializers.ModelSerializer):
    rate = serializers.CharField(max_length=20)

    class Meta:
        model = Rate
        fields = ('rate',)


class MakeAppointment(serializers.ModelSerializer):
    doctor = serializers.CharField(max_length=20)
    patient = serializers.CharField(max_length=20)

    class Meta:
        model = Appointment
        fields = '__all__'


class HistoryOfPatient(serializers.ModelSerializer):
    doctor = serializers.StringRelatedField()
    patient = serializers.StringRelatedField()

    class Meta:
        model = Appointment
        fields = '__all__'


class AverageRate(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = '__all__'


class SendNotification(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'