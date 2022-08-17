from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework import generics, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from patient.models import Patient
from .models import Doctor
from .serializers import RegisterSerializer, LoginSerializer, RegisterProfileDoctor, DoctorProfile, DoctorSerializer
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
      token = get_tokens_for_user(user)
      return Response({'token': token, 'msg': 'Login Success'}, status=status.HTTP_200_OK)
    else:
      return Response({'errors': {'non_field_errors': ['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def doctorprofile(request):
    serializer = RegisterProfileDoctor(data=request.data)
    if serializer.is_valid():
        if 'user' in request.data:
            username = serializer.validated_data['user']
            user = User.objects.get(username=username)
            if user.is_superuser or user.is_staff:
                return Response({'errors': {'non_field_errors': ['you are admin not be a doctor']}},
                                status=status.HTTP_404_NOT_FOUND)
            doctor = Doctor.objects.filter(user=user)
            if doctor:
                return Response({'errors':['this is a doctor already with this name ']}, status=status.HTTP_404_NOT_FOUND)
            patient = Patient.objects.filter(user=user)
            if patient:
               return Response({'errors': ['this is a patient  already with this name or email']},
                         status=status.HTTP_404_NOT_FOUND)
            if 'image' in request.data:
                image = request.data['image']
                serializer.save(user=user, image=image)
            else:
                serializer.save(user=user)
            return Response({'msg': 'sign up is Success as doctor '}, status=status.HTTP_200_OK)
        else:
            return Response({'msg':'must login in your account'})
    else:
        return Response({'errors': {'non_field_errors':['some of data may be not Valid']}}, status=status.HTTP_404_NOT_FOUND)

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

