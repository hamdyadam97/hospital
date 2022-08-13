from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework import generics, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
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



# @api_view(['POST'])
# def signin(request):
#     log = LoginSerializer(data=request.data)
#     if log.is_valid():
#         user = User.objects.filter(username=request.data['username'])
#         if len(user) > 0 and user is not None:
#             authuser = authenticate(username=request.data['username'], password=request.data['password'])
#             login(request, authuser)
#             data = LoginSerializer(User)
#             return Response(data.data, status=HTTP_201_CREATED)
#     else:
#       return Response({'error': 'invalid data'}, status=HTTP_400_BAD_REQUEST)



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
    print(serializer)
    if serializer.is_valid():
        username = serializer.validated_data['user']
        image = request.data['image']
        print(image)
        user = User.objects.get(username=username)
        serializer.save(user=user, image=image)
        return Response({'msg': 'Login Success'}, status=status.HTTP_200_OK)
    else:
        return Response({'errors': {'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_doctor_data(request, username):
    user = User.objects.get(username=username)
    profile = Doctor.objects.get(user=user)
    doc=DoctorProfile(profile)
    return Response(data=doc.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def doctor_view(request):
        queryset = Doctor.objects.all()[0:3]
        serializer_class = DoctorSerializer(queryset,many=True)
        print(serializer_class)
        # return Response(serializer_class.data)
        return Response(data=serializer_class.data, status=status.HTTP_200_OK)

