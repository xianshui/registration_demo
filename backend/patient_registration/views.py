from email import message
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import permissions
from .models import Patient, Appointment
from .serializers import AppointmentSerializer, PatientSerializer, DisplayPatientSerializer
from rest_framework import status
from rest_framework.response import Response

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = DisplayPatientSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

class RegisterView(APIView):
    def post(self, request, format = None):
      print(request.data)
      serializer = PatientSerializer(data=request.data)
      existingPatients = Patient.objects.filter(email = request.data['email'])

      if existingPatients.count() > 0:
        return Response({'code': 0, 'msg': 'User already exist!'}, status=status.HTTP_200_OK)

      if serializer.is_valid():
        serializer.save()
        return Response({'code': 1, 'msg': 'success'}, status=status.HTTP_200_OK)
      else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UploadView(APIView):
    def handle_uploaded_file(self, file):
      with open(f"media/{file.name}", 'wb+') as destination:
          for chunk in file.chunks():
              destination.write(chunk)

    def post(self, request, format = None):
      file_obj = request.data['file']
      self.handle_uploaded_file(file_obj)
      return Response({'path': f"/media/{file_obj.name}"}, status=status.HTTP_200_OK)

    def options(self, request, format = None):
      return Response('', status=status.HTTP_200_OK)

class SignInView(APIView):
    def post(self, request, format = None):
      matched_users = User.objects.filter(email = request.data['email'])

      if matched_users.count() > 0:
        return Response({'code': 1, 'msg': 'success'}, status=status.HTTP_200_OK)
      else:
        return Response({'code': 0, 'msg': 'Email or password not match'}, status=status.HTTP_200_OK)


class SignOutView(APIView):
    def post(self, request, format = None):
      return Response({'code': 1, 'msg': 'success'}, status=status.HTTP_200_OK)
