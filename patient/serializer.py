from rest_framework import serializers
from .models import Patient


class RegisterProfilePatient(serializers.ModelSerializer):
    user = serializers.CharField(max_length=20)
    class Meta:
        model = Patient
        # fields = '__all__'

        fields = ('age','history','gender','mobile','user','image')

class PatientProfile(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields='__all__'
        fields = ('age','history','image','mobile','gender','user',)


class PatientProfile(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
