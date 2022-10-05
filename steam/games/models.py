from django.core.validators import MinValueValidator, MaxValueValidator

from django.db import models

from games.services.enums.choices import ItemTypeChoices, ItemQualityChoices, GameCategoryChoices
from user.models import User


class Application(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=30, choices=GameCategoryChoices.choices)
    size = models.FloatField(default=0, validators=[
        MinValueValidator(limit_value=1),
        MaxValueValidator(limit_value=200000)
    ])
    dev_date = models.DateField()
    description = models.TextField()
    min_system_requirements = models.TextField()
    recommended_system_requirements = models.TextField()
    downloads = models.PositiveIntegerField(default=0, validators=[
        MinValueValidator(limit_value=0),
        MaxValueValidator(limit_value=20000000)
    ])
    publisher = models.ForeignKey(User, on_delete=models.DO_NOTHING,
                                  related_name='Application', related_query_name='Applications')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[
        MinValueValidator(limit_value=0),
        MaxValueValidator(limit_value=10000)
    ])


class Library(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='Library', related_query_name='Libraries')
    application = models.ForeignKey('Application', on_delete=models.CASCADE,
                                    related_name='Library', related_query_name='Libraries')
    game_time = models.PositiveSmallIntegerField(default=0, validators=[
        MinValueValidator(limit_value=0),
        MaxValueValidator(limit_value=100000)
    ])
    last_launch = models.DateTimeField()


class Item(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE,
                                    related_name='Item', related_query_name='Items')
    # price = models.FloatField(default=0, validators=[
    #     MinValueValidator(limit_value=0.03),
    #     MaxValueValidator(limit_value=3000)
    # ])
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=30, choices=ItemTypeChoices.choices)
    quality = models.CharField(max_length=40, choices=ItemQualityChoices.choices)
    description = models.TextField()
    is_sellable = models.BooleanField(default=True)


class GameComment(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING,
                             related_name='GameComment', related_query_name='GameComments')
    application = models.OneToOneField('Application', on_delete=models.CASCADE,
                                   related_name='GameComment', related_query_name='GameComments')
    description = models.TextField()
    grade = models.PositiveSmallIntegerField(default=5, validators=[
        MinValueValidator(limit_value=0),
        MaxValueValidator(limit_value=5)
    ])
