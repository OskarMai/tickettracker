from django.urls import path
from . import views

app_name = "authenticate"
urlpatterns = [
	path("", views.home, name = "home"),
	path("login", views.loginPage, name = "login"),
	path("register", views.registerPage, name="register"),
	path("logout", views.logoutPage, name="logout"),
	path("password_change", views.password_change, name="password_change")
]