from rest_framework import serializers
from .models import Patient


class RegisterProfilePatient(serializers.ModelSerializer):
    user = serializers.CharField(max_length=20, required=True)
    gender = serializers.CharField(max_length=20, required=True)
    class Meta:
        model = Patient
        # fields = '__all__'
        fields = ('age', 'history', 'image', 'mobile', 'gender', 'user',)


class PatientProfile(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Patient
        fields = '__all__'


class UpdateProfilePatient(serializers.ModelSerializer):
    class Mete:
        model = Patient
        fields = ['history', 'mobile', 'image','age']
