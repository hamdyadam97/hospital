from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import Doctor, ISActive


class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50)
    class Meta:
        model = User
        fields = ['username','password']


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        try:
            user = User.objects.create(
                username=validated_data['username'],
                email=validated_data['email'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name']
            )
            user.set_password(validated_data['password'])
            user.save()
        except:
            return Response({'error':'invalid data'},status=HTTP_400_BAD_REQUEST)
        return user


class RegisterProfileDoctor(serializers.ModelSerializer):
    user = serializers.CharField(max_length=20,required=True)
    price = serializers.IntegerField(required=True)
    from_of_work = serializers.IntegerField(required=True)
    to_of_work = serializers.IntegerField(required=True)
    day1_of_work = serializers.CharField(max_length=20, required=True)
    day2_of_work = serializers.CharField(max_length=20, required=True)
    day3_of_work = serializers.CharField(max_length=20, required=True)

    class Meta:
        model = Doctor
        # fields = '__all__'
        fields = ('bio','address','address_detail','birth_date','gender','user',
                  'doctor','specialist_doctor','price','from_of_work','to_of_work','day1_of_work',
                  'day2_of_work','day3_of_work','mobile','facebook','google',
                  'twitter',)


class DoctorProfile(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Doctor
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = Doctor
        # fields = '__all__'
        fields = ('user','doctor','specialist_doctor','image','bio','avg')


class UpdateProfileDoctor(serializers.ModelSerializer):
    # user = serializers.CharField(max_length=20, required=True)
    class Meta:
        model = Doctor
        fields = ['bio', 'address', 'address_detail', 'mobile', 'price','image',]


class CreateNumberActive(serializers.ModelSerializer):
    class Meta:
        model = ISActive
        fields = ['num_verify']