from django import forms
from django.forms import ModelForm
from .models import *
from authenticate.models import NewUser

class ProjectAddForm(forms.Form):

	name = forms.CharField(label='Name', max_length = 64, widget=forms.TextInput(
		attrs={
			'class':'form-control col-sm-3',
		}))
	description = forms.CharField(label = 'Description', max_length=1000, widget=forms.Textarea(
		attrs={
			'class': 'form-control',
			'rows': '5',
		}))

class ProjectDeleteForm(forms.Form):
	project = forms.ModelChoiceField(queryset=Project.objects.all(), label=None)
	project.widget.attrs['class'] = 'form-control'
class AssignProjectForm(forms.Form):
	actionChoices = (
		('0',u'Add'),
		('1',u'Remove')
		)
	project = forms.ModelChoiceField(queryset= Project.objects.all(), label=None)
	project.widget.attrs['class'] = 'form-control'
	member = forms.ModelChoiceField(queryset= NewUser.objects.filter(groups__name__in=['admin','developer']), label=None)
	member.widget.attrs['class']='form-control'
	action = forms.ChoiceField(required = True, choices= actionChoices)
	action.widget.attrs['class']='form-control'

	class Meta:
		model = ProjectMember
		fields = ['project','member']