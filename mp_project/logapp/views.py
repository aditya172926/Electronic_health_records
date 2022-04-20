from django.http import JsonResponse
from django.shortcuts import redirect, render
import ipfsApi


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

def FileUpload(request):
	if request.method == 'POST':
		data = request.POST
		file = request.FILES
		print(data)
		print(file)
		return JsonResponse("FileUpload responding", status=200, safe=False)

def UploadPresFile(request):
	if request.method == "GET":
		print(request.GET["presName"])
		presName = request.GET["presName"]
		treatmentText = request.GET["treatmentName"]
		dose = request.GET["dose"]
		print(treatmentText)
		writePrescription = open(presName + "prescription.txt", "w+")
		writePrescription.write(treatmentText + "\n\n" + "Dose = " + dose)
		writePrescription.close()
		Ipfsapi = ipfsApi.Client('127.0.0.1', 5001)
		Ipfs_response = Ipfsapi.add(presName + "prescription.txt")
		print(Ipfs_response)
		return JsonResponse(Ipfs_response, status=200, safe=False)