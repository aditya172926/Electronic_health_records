from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.AboutPage, name="about"),
    path("signupEntity/", views.EntitySignUp, name="signupEntity"),
    path("prescription/", views.Prescription, name="prescription"),
    path("doctorprofile/", views.GetDoctorProfile, name="doctorprofile")
]