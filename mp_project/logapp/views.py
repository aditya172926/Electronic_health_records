from django.shortcuts import render

def index(request):
	template_name = "logapp/index.html"
	if request.GET.get("n1") and request.GET.get("n2"):
		return render(request, template_name, {"msg":"page rendered"})
	else:
		return render(request, template_name)

def AboutPage(request):
	template_name="logapp/about.html"
	return render(request, template_name, {"msg": "About page loaded"})
	
def PatientSignUp(request):
	template_name="logapp/patient.html"
	return render(request, template_name, {"msg": "Patient page loaded"})

def Prescription(request):
	template_name="logapp/prescription.html"
	return render(request, template_name, {"msg": "Prescription page loaded"})