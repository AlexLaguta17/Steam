from django.db import models


class RoleChoices(models.TextChoices):
    COMPANY = 'COMPANY', 'Company'
    ADMIN = 'ADMIN', 'Admin'
    PLAYER = 'PLAYER', 'Player'
