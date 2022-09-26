from django.contrib.auth.models import UserManager
from django.db import models
from user.services.validators import validators
from django.contrib.auth.base_user import AbstractBaseUser



class User(AbstractBaseUser):
    username = models.CharField('username', max_length=30, unique=True)
    email = models.EmailField('email', max_length=255, unique=True)
    password = models.CharField('password', max_length=500)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # a admin user; non super-user
    is_superuser = models.BooleanField(default=False)  # a superuser
    ver_email = models.BooleanField(null=False, default=False)
    phone_number = models.CharField(max_length=14, validators=[
        validators.validate_phone_number
    ])
    ver_phone = models.BooleanField(null=False, default=False)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["password", "email"]



    def __str__(self):
        return self.email
