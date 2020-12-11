from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated:#prevents user from logging in if they are already logged in
			return redirect("/")
		else:
			return view_func(request, *args, **kwargs)

	return wrapper_func