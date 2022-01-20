from django.shortcuts import render

def home(request):
	if request.GET.get("n1") and request.GET.get("n2"):
		return render(request, "home.html", {"msg":msg})
	else:
		return render(request,"home.html")
	