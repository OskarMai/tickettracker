from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from authenticate.models import NewUser
from .filters import *
from .forms import *
import datetime

# Create your views here.
def index(request):
	ticket_list = Ticket.objects.all()
	context={
		'ticket_list': ticket_list,
	}
	return render(request, "tickets/index.html",context)