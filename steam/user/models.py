from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from user.services.validators import validators


class User(AbstractBaseUser):
    login = models.CharField('login', max_length=30, unique=True)
    email = models.EmailField('email', max_length=255, unique=True)
    password = models.CharField('password', max_length=500)
    ver_email = models.BooleanField(null=False, default=False)
    phone_number = models.CharField(max_length=14, validators=[
        validators.validate_phone_number
    ])
    ver_phone = models.BooleanField(null=False, default=False)

    USERNAME_FIELD = "login"
    REQUIRED_FIELDS = ["password", "email"]

    def __str__(self):
        return self.email
