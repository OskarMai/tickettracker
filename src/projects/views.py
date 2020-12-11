from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from authenticate.models import NewUser
from .filters import *
from .forms import *
# Create your views here.

@login_required(login_url='authenticate:login')
def index(request):
	project_list = Project.objects.all()#all project objects
	project_filter = ProjectFilter(request.GET , queryset= Project.objects.all())
	project_list = project_filter.qs
	context = { 'project_list': project_list, 'project_filter': project_filter
	}
	return render(request, "projects/index.html",context)

@login_required(login_url='authenticate:login')
def add(request):
	form = ProjectAddForm()
	if request.method == "POST":
		project = Project(name=request.POST.get('name'),description=request.POST.get('description'),submitter=request.user)
		project.save()
		return redirect("projects:index")
	context= {
		'form': form
	}
	return render(request, "projects/add.html",context)

@login_required(login_url='authenticate:login')
def personnel(request):
	user_list = NewUser.objects.all()
	user_filter = UserFilter(request.GET,queryset=user_list)
	user_list= user_filter.qs 
	if request.method == "POST":
		form = AssignProjectForm(request.POST)
		if form.is_valid():
			project = form.cleaned_data['project']
			member = form.cleaned_data['member']
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