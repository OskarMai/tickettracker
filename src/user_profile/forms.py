from django import forms
from django.forms import ModelForm
from authenticate.models import NewUser

class EditProfileForm(forms.ModelForm):
	class Meta:
		model = NewUser
		fields = ['pfp','email','user_name','first_name','about']

