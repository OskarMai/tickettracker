from django import forms
from django.forms import ModelForm
from .models import NewUser
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
	class Meta:
		model = NewUser
		fields = ['email', 'user_name', 'first_name']