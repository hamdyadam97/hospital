from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import Patient



class RegisterProfilePatient(serializers.ModelSerializer):
    user = serializers.CharField(max_length=20)
    class Meta:
        model = Patient
        # fields = '__all__'
        fields = ('age','history','gender','mobile','gender','user',)

