from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from authenticate.models import NewUser
from .filters import *
from .forms import *

# Create your views here.
def index(request):
	return render(request, "tickets/index.html")