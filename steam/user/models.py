from django.contrib.auth.models import UserManager, AbstractUser, PermissionsMixin
from django.db import models

from user.services.enums.choices import RoleChoices
from user.services.validators import validators


class User(AbstractUser, PermissionsMixin):
    ver_email = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=14, validators=[
        validators.validate_phone_number
    ])
    role = models.CharField(max_length=7, choices=RoleChoices.choices)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["password", "email"]

    def __str__(self):
        return self.first_name
