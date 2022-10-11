from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from games.models import Item, Application
from user.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='Profile', related_query_name='Profiles')
    description = models.CharField(max_length=800)
    age = models.PositiveSmallIntegerField(default=10, validators=[
        MinValueValidator(limit_value=10),
        MaxValueValidator(limit_value=90)
    ])
    location = models.CharField(max_length=30)
    level = models.PositiveSmallIntegerField(default=0, validators=[
        MinValueValidator(limit_value=0),
        MaxValueValidator(limit_value=3000)
    ])


class UserItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE,
                             related_name='UserItem', related_query_name='UserItems')
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[
        MinValueValidator(limit_value=0.03),
        MaxValueValidator(limit_value=3000)
    ])
    is_on_sale = models.BooleanField(default=False)


class Inventory(models.Model):
    user_item = models.ForeignKey(UserItem, on_delete=models.CASCADE,
                             related_name='Inventory', related_query_name='Inventories')
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='Inventory', related_query_name='Inventories')
    is_tradable = models.BooleanField(default=True)
    on_sale = models.BooleanField(default=False)


class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='Friend', related_query_name='Friends')
    friend = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='Friend+', related_query_name='Friends+')


class Balance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='Balance', related_query_name='Balance')
    balance = models.DecimalField(max_digits=10, decimal_places=2, validators=[
        MinValueValidator(limit_value=0),
        MaxValueValidator(limit_value=100000)
    ])
    pay_card = models.CharField(max_length=16)


class VacBan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='VacBan', related_query_name='VacBans')
    application = models.ForeignKey(Application, on_delete=models.CASCADE,
                                    related_name='VacBan', related_query_name='VacBans')
    for_date = models.DateTimeField(auto_now_add=True)


class ProfileComment(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING,
                             related_name='ProfileComment', related_query_name='ProfileComments')
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE,
                                   related_name='ProfileComment', related_query_name='ProfileComments')
    description = models.TextField()


class BuyRequest(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE,
                             related_name='BuyRequest', related_query_name='BuyRequests')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='BuyRequest', related_query_name='BuyRequests')
    wish_price = models.DecimalField(max_digits=10, decimal_places=2, validators=[
        MinValueValidator(limit_value=0),
        MaxValueValidator(limit_value=3000)
    ])
    amount = models.PositiveSmallIntegerField(default=1, validators=[
        MinValueValidator(limit_value=1),
        MaxValueValidator(limit_value=1000)
    ])
