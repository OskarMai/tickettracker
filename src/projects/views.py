from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from authenticate.models import NewUser
from .filters import *
from .forms import *
# Create your views here.

@login_required(login_url='authenticate:login')#decorator that does not allow access to views when you are not logged in
def index(request):
	project_list = Project.objects.all()#all project objects
	project_filter = ProjectFilter(request.GET , queryset= Project.objects.all())
	project_list = project_filter.qs
	if request.method == "POST":
		form = ProjectAddForm(request.POST)
		if form.is_valid():
			project = Project(name=request.POST.get('name'),description=request.POST.get('description'),submitter=request.user)
			project.save()
			return redirect("projects:index")
		else:
			messages.error(request,"INVALID INPUT")
			context = { 
			'project_list': project_list,
			'project_filter': project_filter,
			'form': ProjectAddForm()
			}
			return render(request, "projects/index.html",context)
	else:
		context = { 
			'project_list': project_list,
			'project_filter': project_filter,
			'form': ProjectAddForm()
		}
		return render(request, "projects/index.html",context)

@login_required(login_url='authenticate:login')
def personnel(request):
	user_list = NewUser.objects.all()#list of all users objects
	user_filter = UserFilter(request.GET,queryset=user_list)
	user_list= user_filter.qs 
	if request.method == "POST":
		form = AssignProjectForm(request.POST)
		if form.is_valid():
			project = form.cleaned_data['project']
			member = form.cleaned_data['member']
			action = form.cleaned_data['action']
			if action == "0":#0 means add
				try:
					assignment = ProjectMember(project= project,member= member)
					assignment.save()
					messages.success(request,"SUCCESSFULLY ADDED " + member.user_name + " TO PROJECT: " + project.name)
					return redirect("projects:personnel")
				except:
					messages.error(request,"SELECTED USER ALREADY ASSIGNED TO PROJECT")
					return render(request, "personnel/index.html",{
					'user_list' : user_list,
					'user_filter': user_filter,
					'form' : AssignProjectForm()
				})
			elif action =="1":#1 means remove
				ProjectMember.objects.filter(project=project, member=member).delete()
				messages.success(request, "SUCCESSFULLY REMOVED " + member.user_name + " FROM PROJECT: " + project.name)
				return redirect("projects:personnel")
		else:
			messages.error(request,"SELECTION IS INVALID")
			return render(request, "personnel/index.html",{
				'user_list' : user_list,
				'user_filter': user_filter,
				'form' : AssignProjectForm()
			})
	else:
		context={
		'user_list' : user_list,
		'user_filter': user_filter,
		'form' : AssignProjectForm()

	}
		return render(request,"personnel/index.html",context)