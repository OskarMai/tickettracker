from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import *
from authenticate.models import NewUser
from .filters import *
from .forms import *
import datetime
from authenticate.decorators import *
from django.contrib.auth.models import Group

# Create your views here.
@login_required(login_url='authenticate:login')
@allowed_users(allowed_roles = ['admin','developer','submitter'])
def index(request):
	ticket_list = Ticket.objects.all()
	ticket_filter = TicketFilter(request.GET,queryset=ticket_list)
	ticket_list = ticket_filter.qs
	context={
		'ticket_list': ticket_list,
		'ticket_filter': ticket_filter,
		'form': SubmitTicketForm(),
	}
	return render(request, "tickets/index.html",context)

@login_required(login_url='authenticate:login')
@allowed_users(allowed_roles = ['admin','developer'])
def details(request,ticket_id):
	ticket = Ticket.objects.get(pk=ticket_id)
	attachmentsList = ticket.ticket_attachments.all()
	comments = ticket.ticket_comments.all()
	memberList = []
	for item in ticket.project.medium_project.all():
		memberList.append(item.member)

	if request.user not in memberList:
		messages.error(request,"USER DOES NOT HAVE ACCESS TO TICKET #: " + str(ticket_id))
		return redirect("tickets:index")
	try:

		ticket = Ticket.objects.get(pk=ticket_id)#find ticket object we got from link
		context = {
			'ticket':ticket,
			'form2': FileForm(),
			'attachmentsList': attachmentsList,
			'form': CommentForm(),
			'comments':comments,
		}
		return render(request, "tickets/details.html",context)
	except:
		messages.error(request,"TICKET DOES NOT EXIST")
		return redirect("tickets:index")

@login_required(login_url='authenticate:login')
@allowed_users(allowed_roles = ['admin','developer','submitter'])
def submit(request):
	if request.method=="POST":
		form = SubmitTicketForm(request.POST)
		if form.is_valid():#adds hidden fields to ticket object
			try:
				project = form.cleaned_data['project']
				description = form.cleaned_data['description']
				submitter = request.user
				priority = "9"#lowest priority
				timeCreated = datetime.datetime.now()
				race = "Bugs/Errors"
				status = "Open"
				ticket = Ticket(project = project, description=description,submitter=submitter,priority=priority,timeCreated=timeCreated,race = race,status = status)
				ticket.save()
				messages.success(request,"SUCCESSFULLY SUBMITTED TICKET")
				return redirect("tickets:index")
			except:
				messages.error(request,"INVALID TICKET SUBMISSION FORMAT")
				return redirect("tickets:index")
		else:
			messages.error(request,"INVALID TICKET SUBMISSION FORMAT")
			return redirect("tickets:index")
		return redirect("tickets:index")
	else:
		context = {
			'form':SubmitTicketForm(),
		}
		return render(request,"tickets/submit.html",context)

@login_required(login_url="authenticate:login")
@allowed_users(allowed_roles = ['admin','developer'])
def edit(request,ticket_id):
	ticket = Ticket.objects.get(pk=ticket_id)
	memberList = []
	for item in ticket.project.medium_project.all():
		memberList.append(item.member)

	if request.user not in memberList:
		messages.error(request,"USER DOES NOT HAVE ACCESS TO TICKET #: " + str(ticket_id))
		return redirect("tickets:index")
	form = EditTicketForm(instance=ticket)
	if request.method=="POST":
		form = EditTicketForm(request.POST, instance=ticket)
		if form.is_valid():
			form.save()
			return redirect("tickets:index")
		else:
			messages.error(request,"INVALID TICKET EDIT")
			return redirect("tickets:index")
	context={
		'form':form
	}
	return render(request,"tickets/edit.html",context)

@login_required(login_url="authenticate:login")
@allowed_users(allowed_roles = ['admin','developer'])
def upload(request,ticket_id):
	if request.method== "POST":
		form = FileForm(request.POST,request.FILES)
		if form.is_valid():
			try:
				ticket = Ticket.objects.get(pk=ticket_id)
				file = File(ticket=ticket,file=request.FILES['file'],description=request.POST['description'])
				file.save()
				messages.success(request,"SUCCESSFULLY ATTACHED FILE TO TICKET")
				return redirect("tickets:details",ticket_id=ticket_id)
			except:
				messages.error(request,"INVALID FILE ATTACHMENT")
				return redirect("tickets:details",ticket_id=ticket_id)
		else:
			messages.error(request,"INVALID FILE ATTACHMENT")
			return redirect("tickets:details",ticket_id=ticket_id)
	else:
		messages.error(request,"POST REQUESTS ONLY")
		return redirect("tickets:details",ticket_id=ticket_id)

@login_required(login_url="authenticate:login")
@allowed_users(allowed_roles = ['admin','developer'])
def comment(request, ticket_id):
	ticket = Ticket.objects.get(pk=ticket_id)
	if request.method =="POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			try:
				comment =  Comment(message=request.POST['message'], commenter=request.user, ticket=ticket)
				comment.save()
				messages.success(request,"SUCCESSFULLY SUBMITTED COMMENT")
				return redirect("tickets:details",ticket_id=ticket_id)

			except:
				messages.error(request,"INVALID COMMENT FORMAT")
				return redirect("tickets:details",ticket_id=ticket_id)
		else:
			messages.error(request,"INVALID COMMENT FORMAT")
			return redirect("tickets:details",ticket_id=ticket_id)
	return redirect("tickets:details",ticket_id=ticket_id)

