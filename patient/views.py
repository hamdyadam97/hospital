from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from account.models import Doctor
from .models import Patient
from .serializer import RegisterProfilePatient, PatientProfile, UpdateProfilePatient


@api_view(['POST'])
def patient_profile(request):
    serializer = RegisterProfilePatient(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data['user']
        user = User.objects.filter(username=username)
        if user:
            if not Patient.objects.filter(user=user[0]):
                if 'image' in request.data:
                    image = request.data['image']
                    if not Doctor.objects.filter(user=user[0]):
                        serializer.save(user=user[0], image=image)
                        return Response({'msg': 'make profile patient is  Success'}, status=status.HTTP_200_OK)
                    else:
                        return Response({'errors': 'maybe profile with this email or username register as doctor'},
                                        status=HTTP_400_BAD_REQUEST)
                else:
                    if not Doctor.objects.filter(user=user[0]):
                        serializer.save(user=user[0],)
                        return Response({'msg': 'make profile patient is  Success'}, status=status.HTTP_200_OK)
                    else:
                        return Response({'errors': 'maybe profile with this email or username register as doctor'},
                                        status=HTTP_400_BAD_REQUEST)
            else:
                return Response({'errors':'may be duplicate profile with this email or username'},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'errors': 'may be not usr with this name or email'},
                            status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'errors': 'may be data error'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_patient_data(request, username):
    user = User.objects.filter(username=username)
    if user:
        profile = Patient.objects.filter(user=user[0])
        if profile:
            pan = PatientProfile(profile[0])
            print(profile[0].age)
            return Response(data=pan.data, status=status.HTTP_200_OK)
        else:
            return Response({'errors': {'non_field_errors':
                                            ['may be user with name not have profile']}},
                            status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'errors': {'non_field_errors': ['may be not user with name']}}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def update_profile_patient(request):
    if 'user' in request.data:
        user = User.objects.filter(username=request.data['user'])
        if user:
            patient = Patient.objects.get(user=user[0])
            profile = UpdateProfilePatient(patient,data=request.data)
            if profile.is_valid():
                profile.save()
                return Response({'msg': 'profile patient is updated'}, status=HTTP_200_OK)
            else:
                return Response({'msg': 'please enter data is valid'}, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'msg': 'please enter data is valid'}, status=HTTP_400_BAD_REQUEST)
    else:
        return Response({'msg': 'please enter data is valid'}, status=HTTP_400_BAD_REQUEST)
