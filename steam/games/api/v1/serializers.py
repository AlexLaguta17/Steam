from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework import serializers

from games.models import Application, Library, Item, GameComment
from games.services.enums.choices import GameCategoryChoices


class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = '__all__'


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class GameCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameComment
        fields = '__all__'


class GetInApplicationInfoSerializer(serializers.Serializer):
    app_name = serializers.CharField(max_length=50, required=False)
    category = serializers.ChoiceField(choices=GameCategoryChoices.choices, required=False)
    price_from = serializers.DecimalField(max_digits=10, decimal_places=2, required=False, validators=[
        MinValueValidator(limit_value=0),
        MaxValueValidator(limit_value=1000)
    ])
    price_to = serializers.DecimalField(max_digits=10, decimal_places=2, required=False, validators=[
        MinValueValidator(limit_value=0),
        MaxValueValidator(limit_value=1001)
    ])
    asc = serializers.BooleanField(required=False)


class GetOutApplicationInfoSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    description = serializers.CharField(max_length=1000)


class GetInUserAppInfoSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    asc_app_name = serializers.BooleanField(required=False)
    desc_app_time = serializers.BooleanField(required=False)


class AppFieldNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('name',)


class GetOutUserAppInfoSerializer(serializers.Serializer):
    application = AppFieldNameSerializer()
    app_time = serializers.IntegerField()


class GetOutTopAppsSerializer(serializers.Serializer):
    application = AppFieldNameSerializer()
    app_time = serializers.IntegerField()
    last_launch = serializers.DateField()
