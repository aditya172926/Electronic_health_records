from xml.etree.ElementInclude import default_loader
from django.db import models

# Create your models here.
class Patient(models.Model):
    patient_wallet_address = models.CharField(max_length=200, default="")
    patient_name = models.CharField(max_length=200, default="")
    patient_resi_address = models.CharField(max_length=200, default="")
    patient_contact_number = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.patient_name

class Doctor(models.Model):
    doctor_wallet_address = models.CharField(max_length=200, default="")
    doctor_name = models.CharField(max_length=200, default="")
    doctor_resi_address = models.CharField(max_length=200, default="")
    doctor_contact_number = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.doctor_name

class Appointments(models.Model):
    appointment_head = models.CharField(max_length=200, default="")
    appointment_details = models.CharField(max_length=200, default="")