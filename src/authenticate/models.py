from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, PermissionsMixin

# Create your models here.
class CustomAccountManager(BaseUserManager):

	def create_user(self, email, user_name,first_name, password, **other_fields):

		if not email:
			raise ValueError(_("You Must Provide An Email Address"))

		email = self.normalize_email(email)
		user = self.model(email=email,user_name=user_name,first_name=first_name, **other_fields)
		user.set_password(password)
		user.save()
		return user 

	def create_superuser(self, email, user_name, first_name, password, **other_fields):

		other_fields.setdefault("is_staff", True)
		other_fields.setdefault("is_superuser", True)
		other_fields.setdefault("is_active", True)

		if other_fields.get("is_staff") is not True:
			raise ValueError(
				"superuser must be assigned to is_staff=True")

		if other_fields.get("is_superuser") is not True:
			raise ValueError(
				"superuser must be assigned to is_superuser=True")

		return self.create_user(email, user_name, first_name, password, **other_fields)


class NewUser(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(_('email address'), unique=True)
	user_name = models.CharField(max_length=150, unique=True)
	first_name = models.CharField(max_length=150, blank=True)
	start_date = models.DateTimeField(default=timezone.now)
	pfp = models.ImageField(default="pfp1.jpg",null=True,blank=True)
	about = models.TextField(_(
		'about'), max_length=150, blank=True)
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)

	objects = CustomAccountManager()

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = ['user_name', 'first_name']

	def __str__(self):
		return self.user_name
