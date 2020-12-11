from django import forms
from django.forms import ModelForm
from .models import *
from authenticate.models import NewUser

class ProjectAddForm(forms.Form):
	name = forms.CharField(label='name', max_length = 64)
	description = forms.CharField(label = 'description', max_length=64)

class AssignProjectForm(forms.Form):
	project = forms.ModelChoiceField(queryset= Project.objects.all(), label=None)
	member = forms.ModelChoiceField(queryset= NewUser.objects.all(), label=None)

	class Meta:
		model = ProjectMember
		fields = ['project','member']