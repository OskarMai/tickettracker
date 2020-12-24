from django.db import models
from django.conf import settings
# Create your models here.

class Project(models.Model):
	submitter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE , related_name= "projects_created")
	name = models.CharField(max_length=64)
	description = models.CharField(max_length=1000)
	class Meta:
		unique_together = ["name", 'submitter']

	def __str__(self):
		return u'{0}'.format(str(self.id) + ": " + self.name)

class ProjectMember(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE,related_name="medium_project")
	member = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="medium_member")
	class Meta:
		unique_together = ["project","member"]

	def __str__(self):
		return u'{0}'.format(self.member)