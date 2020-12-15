from django import forms
from django.forms import ModelForm
from .models import *


class SubmitTicketForm(forms.Form):
	project = forms.ModelChoiceField(queryset= Project.objects.all(), label=None)
	description = forms.CharField(max_length=1000, label="Describe the issue")

	class Meta:
		model = Ticket
		fields = ['project','description']

class EditTicketForm(forms.ModelForm): #creating a master ticket form with all fields shown and only using it to update ticket objects
	class Meta:
		model = Ticket
		fields = '__all__'

class FileForm(forms.Form):
	file = forms.FileField(label='Select a file',)

class CommentForm(forms.Form):
	message = forms.CharField(max_length = 100)