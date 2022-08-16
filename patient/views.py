from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Patient
from .serializer import RegisterProfilePatient, PatientProfile


@api_view(['POST'])
def pateintprofile(request):
    serializer = RegisterProfilePatient(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data['user']
        image = request.data['image']
        user = User.objects.get(username=username)
        serializer.save(user=user,image=image)
        return Response({'msg':'register Success'}, status=status.HTTP_200_OK)
    else:
        return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_patient_data(request,username):
    user = User.objects.get(username=username)
    profile = Patient.objects.get(user=user)
    pan = PatientProfile(profile)
    return Response(data=pan.data,status=status.HTTP_200_OK)


