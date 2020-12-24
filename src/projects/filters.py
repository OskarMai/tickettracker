import django_filters
from django import forms
from django_filters import CharFilter, ModelChoiceFilter
from .models import *
from authenticate.models import *

class ProjectFilter(django_filters.FilterSet):
	submitter = ModelChoiceFilter(field_name="submitter", queryset=NewUser.objects.all(),widget=forms.Select(
		attrs={
			'class':'form-control col-sm-12'
		}))
	name = CharFilter(field_name="name", lookup_expr='icontains',widget=forms.TextInput(
		attrs={
			'class':'form-control col-sm-12'
		}))
	description = CharFilter(field_name="description", lookup_expr='icontains',widget=forms.TextInput(
		attrs={
			'class':'form-control col-sm-12'
		}))
	class Meta:
		model = Project
		fields = '__all__'

class UserFilter(django_filters.FilterSet):
	username = CharFilter(field_name="user_name", lookup_expr="icontains",widget=forms.Select(
		attrs={
			'class':'form-control'
		}))
	email = CharFilter(field_name="email", lookup_expr="icontains",widget=forms.TextInput(
		attrs={
			'class':'form-control'
		}))
	class Meta:
		model: NewUser
		fields = '__all__'