from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.AboutPage, name="about"),
    path("patient/", views.PatientSignUp, name="patient"),
    path("prescription/", views.Prescription, name="prescription")
]