from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

def user_signup(request):
	if request.method == "POST":
		un = request.POST.get("un")
		pw1 = request.POST.get("pw1")
		pw2 = request.POST.get("pw2")
		if pw1 == pw2:
			try:
				usr = User.objects.get(username=un)
				return render(request, "user_signup.html",{"msg":"user already exists"})
			except User.DoesNotExist:
				usr = User.objects.create_user(username=un, password=pw1)
				usr.save()
				usr = authenticate(username = un, password = pw1)
				if usr is None:
					return render(request, "user_signup.html", {"msg": "Something went wrong! Please try to login directly."})
				login(request, usr)
				return redirect("index")
		else:
			return render(request, "user_signup.html", {"msg":"Passwords don't match."})
	else:
		return render(request,"user_signup.html")


def user_login(request):
	if request.method == "POST":
		un = request.POST.get("un")
		pw = request.POST.get("pw")
		usr = authenticate(username=un, password=pw)
		if usr is None:
			return render(request,"user_login.html", {"msg":"invalid login"})
		else:
			login(request, usr)
			return redirect("index")
	else:
		return render(request, "user_login.html")


def user_logout(request):
	logout(request)
	return redirect("user_login")
				
