import datetime
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
from patient.models import Patient
from .models import Appointment, Notification
from account.models import Doctor
from .serializers import DoctorRate, MakeAppointment, HistoryOfPatient, SendNotification


@api_view(['POST'])
def rate(request, doctor):
    serializer = DoctorRate(data=request.data)
    if serializer.is_valid():
        user = User.objects.get(username=doctor)
        doctor = Doctor.objects.get(user=user)
        patient = request.data['patient']
        user = User.objects.get(username=patient)
        patient = Patient.objects.get(user=user)
        appoint = Appointment.objects.filter(doctor=doctor, patient=patient)
        if appoint:
            if appoint[0].done:
                serializer.save(doctor=doctor, patient=patient)
                return Response({'msg': 'rate Success'}, status=HTTP_200_OK)
            else:
                return Response({'msg': ' no can rate this doctor appointment no yet'}, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({'msg': ' you canit rate this doc'}, status=HTTP_400_BAD_REQUEST)
    else:
        return Response({'msg':' no can rate this doctor'}, status=HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def make_appointment(request):
    serializer = MakeAppointment(data=request.data)
    if serializer.is_valid():
        appointment = True
        name_doctor = request.data['doctor']
        name_patient = request.data['patient']
        user = User.objects.get(username=name_doctor)
        doctor_profile = Doctor.objects.get(user=user)
        patient = User.objects.get(username=name_patient)
        patient = Patient.objects.get(user=patient)
        day = datetime.datetime.now().date()
        print(doctor_profile)
        print(patient)
        while appointment:
            day_of_work = []
            doctor = Appointment.objects.filter(doctor=doctor_profile, date_appointment=day)
            if len(doctor) == 0:
                day_of_work.append(doctor_profile.day1_of_work)
                day_of_work.append(doctor_profile.day2_of_work)
                day_of_work.append(doctor_profile.day3_of_work)
                if day.strftime("%A") in day_of_work:
                    hour = len(doctor) * .5 + int(doctor_profile.from_of_work)
                    serializer.save(doctor=doctor_profile, patient=patient, date_appointment=day,hour=hour,day=day.strftime("%A"))
                    return Response({'msg': day.strftime("%A"),'hour': hour,'date':day}, status=HTTP_200_OK)
                else:
                    day = day + datetime.timedelta(days=1)
                    continue
            if len(doctor) == (doctor_profile.to_of_work-doctor_profile.from_of_work)*2:
                day = day + datetime.timedelta(days=1)
                continue
            else:
                hour = len(doctor) * .5 + int(doctor_profile.from_of_work)
                serializer.save(doctor=doctor_profile, patient=patient, date_appointment=day,hour=hour,day=day.strftime("%A"))
                return Response({'msg': day.strftime("%A"),'hour':hour,'date':day}, status=HTTP_200_OK)
    else:
        return Response({'msg': 'erooo'}, status=HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def history_of_patient(request, patient):
    user = User.objects.get(username=patient)
    history = Patient.objects.get(user=user)
    history = Appointment.objects.filter(patient=history)
    data = HistoryOfPatient(history, many=True)
    return Response(data=data.data,status=HTTP_200_OK)

@api_view(['GET'])
def cancel_appointment(request, id):
    appointment = Appointment.objects.get(id=id)
    if appointment.date_appointment > datetime.datetime.now().date():
        appointment.delete()
        history = Appointment.objects.filter(patient=appointment.patient)
        if history:
            data = HistoryOfPatient(history, many=True)
            return Response(data=data.data, status=HTTP_200_OK)
        else:
            return Response({'msg': 'no appointment for you'}, status=HTTP_400_BAD_REQUEST)
    else:
        return Response({'msg': 'cant delete this'}, status=HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def send_note(request, id):
    appointment = Appointment.objects.get(id=id)
    email = appointment.patient.user.email
    send_mail(
        f'appointment with doctor {appointment.doctor} ',
        f'we are very sorry  {appointment.patient}'
        f' appointment with doctor {appointment.doctor} cancelled ',
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
    Appointment.objects.filter(id=id).update(cancel=True)
    Notification.objects.create(app=appointment,msg=f'appointment cancelled by doc'
                                                    f' {appointment.doctor}',owner=appointment.patient.user.username)
    return Response({"msg":"the appointment is cancelled"},status=HTTP_200_OK)

@api_view(['GET'])
def history_of_doctor(request, username):
    user = User.objects.get(username=username)
    doctor = Doctor.objects.get(user=user)
    appointment_of_doctor = Appointment.objects.filter\
        (doctor=doctor, done=False, cancel=False, date_appointment__gte=datetime.datetime.now().date())
    data = HistoryOfPatient(appointment_of_doctor, many=True)
    return Response(data=data.data, status=HTTP_200_OK)


@api_view(['GET'])
def make_appointment_done(request, id):
    appointment = Appointment.objects.get(id=id)
    email = appointment.patient.user.email
    send_mail(
        f'appointment with doctor {appointment.doctor}',
        f'appointment with doctor  {appointment.doctor}'
        f' you can rate him  ',
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
    Appointment.objects.filter(id=id).update(done=True)
    Notification.objects.create(app=appointment, msg=f'appointment done by doc'
                                                     f' {appointment.doctor}',owner=appointment.patient.user.username)
    return Response({"msg": "the appointment is done"}, status=HTTP_200_OK)


@api_view(['GET'])
def send_notification(request,username):
    noti = Notification.objects.filter(owner=username, read=False)
    cont = noti.count()
    data = SendNotification(noti, many=True)
    return Response({'data':data.data, 'cnt':cont}, status=HTTP_200_OK)