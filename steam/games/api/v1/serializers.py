from rest_framework import serializers

from games.models import Application, Library, Item, GameComment


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
