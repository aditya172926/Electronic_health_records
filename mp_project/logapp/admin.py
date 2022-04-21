from django.contrib import admin
from .models import Patient, Doctor, Appointments

admin.site.site_header = "Electronic Health Records"

# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display = (
        'patient_wallet_address',
        'patient_name',
        'patient_resi_address',
        'patient_contact_number'
    )

class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        'doctor_wallet_address',
        'doctor_name',
        'doctor_resi_address',
        'doctor_contact_number'
    )

admin.site.register(Patient, PatientAdmin)
admin.site.register(Doctor, DoctorAdmin)