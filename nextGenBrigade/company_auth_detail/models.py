from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
# from rest_framework.authtoken.models import Token

class CompanyCUserManager(BaseUserManager):
    def create_user(self, company_email, password=None, **extra_fields):
        if not company_email:
            raise ValueError('Email is required')
        company_email = self.normalize_email(company_email)
        user = self.model(company_email=company_email, **extra_fields)
        user.set_password(password)
        # print("SAVING THE PASSWORD")
        # user.is_staff = True
        user.save()
        return user

    def create_superuser(self, company_email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(company_email, password, **extra_fields)

# Create your models here.
class CustomCompanyUser(AbstractBaseUser,PermissionsMixin):
    company_email = models.EmailField(unique=True)
    company_name = models.CharField(max_length=50)
    company_phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    zipcode = models.CharField(max_length=10, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CompanyCUserManager()

    USERNAME_FIELD = 'company_email'
    REQUIRED_FIELDS = ['company_name','company_phone_number','address']

    def __str__(self):
        return self.company_name