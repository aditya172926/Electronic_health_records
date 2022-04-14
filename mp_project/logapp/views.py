from django.http import JsonResponse
from django.shortcuts import redirect, render

def index(request):
	template_name = "logapp/index.html"
	if request.GET.get("n1") and request.GET.get("n2"):
		return render(request, template_name, {"msg":"page rendered"})
	else:
		return render(request, template_name)

def AboutPage(request):
	template_name="logapp/about.html"
	return render(request, template_name, {"msg": "About page loaded"})
	
def EntitySignUp(request):
	template_name="logapp/signupEntity.html"
	return render(request, template_name, {"msg": "signupEntity page loaded"})

def Prescription(request):
	template_name="logapp/prescription.html"
	return render(request, template_name, {"msg": "Prescription page loaded"})

def LoadDoctorPage(request):
	template_name = "logapp/doctor.html"
	return render(request, template_name, {"msg": "doctor is loaded"})

def GetDoctorProfile(request):
	if request.method == 'GET':
		doctordata = request.GET
		template_name = "logapp/doctor.html"
		print(doctordata)
		return JsonResponse("doctordata", status=200, safe=False)