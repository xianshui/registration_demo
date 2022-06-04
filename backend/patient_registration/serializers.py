from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Patient, Appointment

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['name', 'email', 'password', 'phone_number', 'address', 'photo', 'appointment_time']

class DisplayPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['name', 'email', 'phone_number', 'address', 'photo', 'appointment_time']

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['user', 'time']
