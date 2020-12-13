from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from authenticate.models import NewUser
from .filters import *
from .forms import *
import datetime

# Create your views here.
@login_required(login_url='authenticate:login')
def index(request):
	ticket_list = Ticket.objects.all()
	ticket_filter = TicketFilter(request.GET,queryset=ticket_list)
	ticket_list = ticket_filter.qs
	context={
		'ticket_list': ticket_list,
		'ticket_filter': ticket_filter,
	}
	return render(request, "tickets/index.html",context)

@login_required(login_url='authenticate:login')
def details(request,ticket_id):
	try:

		ticket = Ticket.objects.get(pk=ticket_id)#find ticket object we got from link
		context = {
			'ticket':ticket
		}
		return render(request, "tickets/details.html",context)
	except:
		messages.error(request,"TICKET DOES NOT EXIST")
		return redirect("tickets:index")