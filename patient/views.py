from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from account.models import Doctor
from .models import Patient
from .serializer import RegisterProfilePatient, PatientProfile


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
                        return Response({'errors': {'non_field_errors':
                                                        ['maybe profile with this email or username register as doctor']}},
                                        status=HTTP_400_BAD_REQUEST)
                else:
                    if not Doctor.objects.filter(user=user[0]):
                        serializer.save(user=user[0],)
                        return Response({'msg':'make profile patient is  Success'}, status=status.HTTP_200_OK)
                    else:
                        return Response({'errors': {'non_field_errors':
                                                        ['maybe profile with this email or username register as doctor']}},
                                        status=HTTP_400_BAD_REQUEST)
            else:
                return Response({'errors': {'non_field_errors':
                                                ['may be duplicate profile with this email or username']}},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'errors': {'non_field_errors':
                                            ['may be not usr with this name or email']}},
                            status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'errors':{'non_field_errors': ['may be data error']}}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_patient_data(request, username):
    user = User.objects.filter(username=username)
    if user:
        profile = Patient.objects.get(user=user[0])
        pan = PatientProfile(profile)
        return Response(data=pan.data,status=status.HTTP_200_OK)
    else:
        return Response({'errors': {'non_field_errors': ['may be not user with name']}}, status=status.HTTP_404_NOT_FOUND)

