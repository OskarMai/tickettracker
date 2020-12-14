from django.urls import path
from . import views


app_name='projects'
urlpatterns = [
	path('', views.index, name="index"),
	path('delete/',views.delete, name="delete"),
	path('personnel/',views.personnel, name="personnel"),
]