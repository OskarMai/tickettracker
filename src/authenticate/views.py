from django.shortcuts import render,redirect,reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from .forms import CreateUserForm
from .decorators import *
from django.contrib.auth.models import Group
# Create your views here.
@login_required(login_url='authenticate:login')#deocrator that redirects users to login page if they are not logged in
def home(request):
	return render(request,"authenticate/home.html")

@unauthenticated_user
def registerPage(request):
	form = CreateUserForm()
	if request.method == "POST":
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('user_name')
			messages.success(request,"Successfully registered " + username)
			return redirect("authenticate:login")
	context = {
		"form": form
	}
	return render(request, "authenticate/register.html", context)


@unauthenticated_user
def loginPage(request):
	if request.method == "POST":
		email = request.POST.get('email')
		password = request.POST.get('password')
		user = authenticate(email=email,password= password)
		if user is not None:
			login(request,user)

			return redirect("/")
		else:
			messages.info(request,"Incorrect Login Information")
	context = {}
	return render(request, "authenticate/login.html",context)


@login_required(login_url='authenticate:login')#deocrator that redirects users to login page if they are not logged in
def logoutPage(request):#logs users out
	logout(request)
	return render(request, "authenticate/login.html")


@login_required(login_url='authenticate:login')#deocrator that redirects users to login page if they are not logged in
def password_change(request):
	if request.method == "POST":
		form = PasswordChangeForm(request.user, request.POST)
		if form.is_valid():
			user = form.save()
			update_session_auth_hash(request,user)
			messages.success(request, "Your password was successfully updated")
			return redirect("authenticate:logout")
		else:
			messages.error(request, "Please correct the error below")

	else:
		form = PasswordChangeForm(request.user)

	return render(request, "authenticate/passwordChange.html",{
			'form': form
		})