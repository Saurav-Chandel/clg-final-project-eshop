from django.db import  models
from django.core.validators import MinLengthValidator

import datetime

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.utils.timezone import now
# from store import choices


# Create your models here.


# class AppUserManager(UserManager):
#     def get_by_natural_key(self, username):
#         return self.get(email__iexact=username)

#     def create_user(self, email, password=None, **extra_fields):
#         extra_fields.setdefault("is_staff", False)
#         extra_fields.setdefault("is_superuser", False)
#         return self._create_user(email, password, **extra_fields)

#     def _create_user(self, email, password, **extra_fields):
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         """
#         Create a Super Admin. Not to be used by any API. Only used for django-admin command.
#         :param email:
#         :param password:
#         :param extra_fields:
#         :return:
#         """
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)
#         extra_fields.setdefault('is_active', True)

#         user = self._create_user(email, password, **extra_fields)
#         return user


# class User(AbstractUser):
#     first_name = models.CharField(
#         max_length=200, default=None, null=True, blank=True
#     )
#     email=models.EmailField(unique=True,null=False)
#     phone_no = models.CharField(
#         max_length=20, default=None, null=True, blank=True
#     )
#     email_verified = models.BooleanField(default=False)
#     email_otp = models.CharField(max_length=10, null=True, blank=True)

#     is_deleted = models.BooleanField(default=False)

#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     USERNAME_FIELD = 'email'

#     REQUIRED_FIELDS = ['username']
    
#     manager = AppUserManager()

#     def __str__(self):
#         return self.email
  


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False


    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return  False


