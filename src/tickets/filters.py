import django_filters
from django_filters import CharFilter
from .models import *
from authenticate.models import *
from django import forms

class TicketFilter(django_filters.FilterSet):
	ID = CharFilter(field_name="id", lookup_expr='icontains',label='Ticket #',widget=forms.TextInput(
		attrs={
			'class':'form-control col-sm-12 m-2'
		}))
	Assigned_Project = CharFilter(field_name="project__name", lookup_expr='icontains',label='Project name',widget=forms.TextInput(
		attrs={
			'class':'form-control col-sm-12 m-2'
		}))
	Submitter = CharFilter(field_name="submitter__user_name",lookup_expr='icontains',label='Submitted by',widget=forms.TextInput(
		attrs={
			'class':'form-control col-sm-12 m-2'
		}))
	Priority = CharFilter(field_name='priority',lookup_expr='icontains',label='Priority',widget=forms.TextInput(
		attrs={
			'class':'form-control col-sm-12 m-2'
		}))
	Status = CharFilter(field_name='status',lookup_expr='icontains',label='Status',widget=forms.TextInput(
		attrs={
			'class':'form-control col-sm-12 m-2'
		}))
	class Meta:
		model = Ticket
		exclude = ['lastEdited', 'priority','race','timeCreated','id','submitter','project','personnel','status','description']
