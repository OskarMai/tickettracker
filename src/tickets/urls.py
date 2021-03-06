from django.urls import path
from . import views


app_name='tickets'
urlpatterns = [
	path('', views.index, name="index"),
	path('details/<int:ticket_id>/', views.details,name="details"),
	path('submit/',views.submit,name="submit"),
	path('edit/<int:ticket_id>/',views.edit,name='edit'),
	path('upload/<int:ticket_id>/',views.upload,name='upload'),
	path('comment/<int:ticket_id>/',views.comment,name='comment')
]
