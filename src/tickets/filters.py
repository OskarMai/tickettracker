import django_filters
from django_filters import CharFilter
from .models import *
from authenticate.models import *

class TicketFilter(django_filters.FilterSet):
	ID = CharFilter(field_name="id", lookup_expr='icontains',label='Ticket #')
	Assigned_Project = CharFilter(field_name="project", lookup_expr='icontains',label='project name')
	Submitter = CharFilter(field_name="submitter",lookup_expr='icontains',label='submitted by')
	Priority = CharFilter(field_name='priority',lookup_expr='icontains',label='priority')
	Status = CharFilter(field_name='status',lookup_expr='icontains',label='status')
	class Meta:
		model = Ticket
		exclude = ['lastEdited', 'priority','race','timeCreated','id','submitter','project','personnel','status','description']
