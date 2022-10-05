from django.contrib.auth.models import UserManager, AbstractUser, PermissionsMixin
from django.db import models

from user.services.validators import validators


class User(AbstractUser, PermissionsMixin):
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=14, validators=[
        validators.validate_phone_number
    ])

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["password", "email", "birth_date"]

    def __str__(self):
        return self.first_name
