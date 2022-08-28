from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import generics, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response



from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from account.models import Doctor
from .models import Patient
from .serializer import RegisterProfilePatient, PatientProfile


from .models import Patient
from .serializer import RegisterProfilePatient, PatientProfile,UpdateProfilePatient


@api_view(['GET'])
def get_patient_data(request,username):
    user=User.objects.get(username=username)
    profile=Patient.objects.get(user=user)
    pan=PatientProfile(profile)
    return Response(data=pan.data,status=status.HTTP_200_OK)

@api_view(['POST'])
def patient_profile(request):
    serializer = RegisterProfilePatient(data=request.data)
    print(serializer)
    if serializer.is_valid():
        username = serializer.validated_data['user']
        user = User.objects.filter(username=username)
        if user:
            if not Patient.objects.filter(user=user[0]):
                if 'image' in request.data:
                    image = request.data['image']
                    if not Doctor.objects.filter(user=user[0]):
                        serializer.save(user=user[0], image=image)
                        return Response({'msg': 'Make profile patient is  Success'}, status=status.HTTP_200_OK)
                    else:
                        return Response({'errors': 'Maybe profile with this email or username register as doctor'},
                                        status=HTTP_400_BAD_REQUEST)
                else:
                    if not Doctor.objects.filter(user=user[0]):
                        serializer.save(user=user[0],)
                        return Response({'msg': 'Make profile patient is  Success'}, status=status.HTTP_200_OK)
                    else:
                        return Response({'errors': 'Maybe profile with this email or username register as doctor'},
                                        status=HTTP_400_BAD_REQUEST)
            else:
                return Response({'errors':'May be duplicate profile with this email or username'},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'errors': 'May be not usr with this name or email'},
                            status=status.HTTP_404_NOT_FOUND)
    else:
        return Response({'errors': 'Gender is must choose'}, status=status.HTTP_404_NOT_FOUND)

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
                return Response({'msg':'Profile patient is updated'}, status=HTTP_200_OK)
            else:
                return Response({'msg':'Please enter data is valid'}, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'msg': 'Please enter data is valid'}, status=HTTP_400_BAD_REQUEST)
    else:
        return Response({'msg': 'Please enter data is valid'}, status=HTTP_400_BAD_REQUEST)