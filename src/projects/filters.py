import django_filters
from django_filters import CharFilter
from .models import *
from authenticate.models import *

class ProjectFilter(django_filters.FilterSet):
	name = CharFilter(field_name="name", lookup_expr='icontains')
	description = CharFilter(field_name="description", lookup_expr='icontains')
	class Meta:
		model = Project
		fields = '__all__'

class UserFilter(django_filters.FilterSet):
	username = CharFilter(field_name="user_name", lookup_expr="icontains")
	email = CharFilter(field_name="email", lookup_expr="icontains")
	class Meta:
		model: NewUser
		fields = '__all__'