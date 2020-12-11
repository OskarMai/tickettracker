from django.urls import path
from . import views


app_name='projects'
urlpatterns = [
	path('', views.index, name="index"),
	path('add',views.add, name="add"),
	path('personnel',views.personnel, name="personnel"),
]