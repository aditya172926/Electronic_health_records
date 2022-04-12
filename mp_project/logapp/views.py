from django.shortcuts import render

def index(request):
	if request.GET.get("n1") and request.GET.get("n2"):
		return render(request, "index.html", {"msg":msg})
	else:
		return render(request,"index.html")
	