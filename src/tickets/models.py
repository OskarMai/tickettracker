from django.db import models
from django.conf import settings
from projects.models import *
import datetime
# Create your models here.
class Ticket(models.Model):
	priorityChoices = (
		('1','1'),
		('2','2'),
		('3','3'),
		('4','4'),
		('5','5'),
		('6','6'),
		('7','7'),
		('8','8'),
		('9','9'),
		
	)
	statusChoices = (
		('0','Closed'),
		('1','Open'),

	)
	raceChoices = (
		('0','Bugs/Errors'),
	)
	project = models.ForeignKey(Project, on_delete=models.CASCADE,related_name="project_tickets")
	personnel = models.ForeignKey(ProjectMember, on_delete=models.SET_NULL , related_name="assigned_ticket" , null=True)
	description = models.CharField(max_length=100)
	priority = models.CharField(max_length=100,choices= priorityChoices)
	status = models.CharField(max_length=100, choices = statusChoices)
	race = models.CharField(max_length=100,choices = raceChoices)
	timeCreated = models.DateTimeField(auto_now_add=True)
	lastEdited = models.DateTimeField(default = datetime.datetime(2020,1,1,0,0,0))