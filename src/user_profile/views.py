from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url='authenticate:login')
def index(request):
	user = request.user
	#if request.method=="POST":

	context={
		'user': user,
	}
	return render(request,"profile/index.html",context)


@login_required(login_url='authenticate:login')
def edit(request):
	user = request.user
	form = EditProfileForm(instance = user)
	if request.method=="POST":
		form = EditProfileForm(request.POST,request.FILES, instance=user)
		if form.is_valid():
			form.save()
			print("saved")
			messages.success(request,"SUCCESSFULLY EDITED PROFILE")
			return redirect("user_profile:index")
		else:
			messages.error(request,"INVALID EDIT SUBMITTED")
	context={
		'form':form
	}
	return render(request,"profile/edit.html",context)