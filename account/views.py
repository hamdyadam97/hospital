import datetime
import random
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from rest_framework import generics, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView
from patient.models import Patient
from .models import Doctor, ISActive
from .serializers import RegisterSerializer, LoginSerializer, RegisterProfileDoctor, DoctorProfile, DoctorSerializer, \
    UpdateProfileDoctor, CreateNumberActive
from rest_framework_simplejwt.tokens import RefreshToken
from .renderers import UserRenderer
app_name = 'account'


def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }


class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer


class UserLoginView(APIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.data.get('username')
    password = serializer.data.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        us = User.objects.get(username=username)
        if not us.is_staff:
            token = get_tokens_for_user(user)
            doc = Doctor.objects.filter(user=us)
            pat = Patient.objects.filter(user=us)
            if doc:
                return Response({'token': token, 'msg': 'Login Success','doc':"doctor"}, status=status.HTTP_200_OK)
            if pat:
                return Response({'token': token, 'msg': 'Login Success','doc':"patient"}, status=status.HTTP_200_OK)
        else:
            return Response({'errors': 'may your ara admin'}, status=status.HTTP_404_NOT_FOUND)

    else:
        return Response({'errors': 'Email or Password is not Valid'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def doctorprofile(request):
    serializer = RegisterProfileDoctor(data=request.data)
    if serializer.is_valid():
        if 'user' in request.data:
            username = serializer.validated_data['user']
            user = User.objects.get(username=username)
            if user.is_superuser or user.is_staff:
                return Response({'errors':  'you are admin not be a doctor'},
                                status=status.HTTP_404_NOT_FOUND)
            doctor = Doctor.objects.filter(user=user)
            if doctor:
                return Response({'errors':'this is a doctor already with this name '}, status=status.HTTP_404_NOT_FOUND)
            patient = Patient.objects.filter(user=user)
            if patient:
                return Response({'errors': 'this is a patient  already with this name or email'},
                         status=status.HTTP_404_NOT_FOUND)
            if 'image' in request.data:
                image = request.data['image']
                serializer.save(user=user, image=image)
                return Response({'msg': 'sign up is Success as doctor '}, status=status.HTTP_200_OK)
            else:
                serializer.save(user=user)
            return Response({'msg': 'sign up is Success as doctor '}, status=status.HTTP_200_OK)
        else:
            return Response({'msg':'must login in your account'})
    else:
        return Response({'errors': 'some of data may be not Valid'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_doctor_data(request, username):
    user = User.objects.filter(username=username)
    if user:
        profile = Doctor.objects.filter(user=user[0])[0]
        if profile:
            doc = DoctorProfile(profile)
            return Response(data=doc.data, status=status.HTTP_200_OK)
        else:
            return Response({"msg": "user not have  profile"}, status=HTTP_400_BAD_REQUEST)
    else:
        return Response({"msg": "user here"}, status=HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def doctor_view(request):
        queryset = Doctor.objects.all()
        serializer_class = DoctorSerializer(queryset,many=True)
        return Response(data=serializer_class.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_profile_doctor(request):
    if 'user' in request.data:
        user = User.objects.filter(username=request.data['user'])
        if user:
            doc = Doctor.objects.filter(user=user[0])
            profile = UpdateProfileDoctor(doc, data=request.data)
            if profile.is_valid():
                profile.save()
                return Response({'msg': 'successful update profile doctor'}, status=HTTP_200_OK)
            else:
                return Response({'msg': 'please enter data valid'}, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'msg': 'please enter data valid'}, status=HTTP_400_BAD_REQUEST)

    else:
        return Response({'msg': 'please enter data valid'}, status=HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def create_verify_num(requset, username):
    user = User.objects.get(username=username)
    n = random.randint(1000, 9999)
    email = user.email
    send_mail(
        f'you can verify email',
        f'appointment with doctor{n}',
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
    ISActive.objects.create(user_active=user, num_verify=n)
    return Response({'number': n}, status=HTTP_200_OK)
@api_view(['PUT'])
def verify_num(request,username):
    user = User.objects.get(username=username)
    isactive = ISActive.objects.get(user_active=user)
    active = CreateNumberActive(isactive, data=request.data)
    if active.is_valid():
        print(isactive.expire_date)
        if isactive.num_verify == int(request.data['num']) and isactive.expire_date >= datetime.datetime.now(datetime.timezone.utc):
            active.save(is_active=True)
            return Response({'msg':'congratulations'},status=HTTP_200_OK)
        else:
            return Response({'msg': 'num no  right'}, status=HTTP_400_BAD_REQUEST)
    else:
        return Response({'msg': 'not valid data'}, status=HTTP_400_BAD_REQUEST)

