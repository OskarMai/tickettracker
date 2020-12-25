from django import forms
from django.forms import ModelForm
from .models import *


class SubmitTicketForm(forms.Form):
	project = forms.ModelChoiceField(queryset= Project.objects.all(), label=None)
	description = forms.CharField(max_length=1000, label="Describe the issue",widget=forms.Textarea(
		attrs={
			'rows':'4'
		}))
	project.widget.attrs['class']='form-control col-sm-12'
	description.widget.attrs['class']='form-control col-sm-12'
	class Meta:
		model = Ticket
		fields = ['project','description']

class EditTicketForm(forms.ModelForm): #creating a master ticket form with all fields shown and only using it to update ticket objects
	class Meta:
		model = Ticket
		fields = '__all__'
class FileForm(forms.Form):
	file = forms.FileField(label='Select a file',)
	description = forms.CharField(max_length=100,widget=forms.TextInput(
		attrs={
			'class':'form-control col-sm-12'
		}))

class CommentForm(forms.Form):
	message = forms.CharField(max_length = 100,widget=forms.TextInput(
		attrs={
			'class':'form-control col-sm-12'
		}))