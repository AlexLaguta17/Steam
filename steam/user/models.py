from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from user.services.validators import validators


class User(AbstractBaseUser):
    login = models.CharField(max_length=30)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    ver_email = models.BooleanField(null=False, default=False)
    phone_number = models.CharField(max_length=14, validators=[
        validators.validate_phone_number
    ])
    ver_phone = models.BooleanField(null=False, default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'password']

    def __str__(self):
        return self.email
