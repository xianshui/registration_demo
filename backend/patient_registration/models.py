from unicodedata import name
from django.db import models

class Patient(models.Model):
  appointment_time = models.CharField(max_length=32)
  name = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  password = models.CharField(max_length=16)
  phone_number = models.CharField(max_length=255)
  address = models.TextField()
  photo = models.TextField()

  def __str__(self):
        return self.name


class Appointment(models.Model):
  patient = models.IntegerField()
  time = models.DateTimeField()

  def __str__(self):
        return self.name
