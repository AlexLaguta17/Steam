from rest_framework import serializers

from account.models import Profile, Inventory, Friend, Balance, VacBan, ProfileComment, BuyRequest


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'


class InventorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventory
        fields = '__all__'


class FriendSerializer(serializers.ModelSerializer):

    class Meta:
        model = Friend
        fields = '__all__'


class BalanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Balance
        fields = '__all__'


class VacBanSerializer(serializers.ModelSerializer):

    class Meta:
        model = VacBan
        fields = '__all__'


class ProfileCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProfileComment
        fields = '__all__'


class BuyRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = BuyRequest
        fields = '__all__'
