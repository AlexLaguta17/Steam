from rest_framework import serializers

from account.models import Profile, Inventory, Friend, Balance, VacBan, ProfileComment, BuyRequest
from games.api.v1.serializers import ApplicationSerializer, ItemSerializer
from games.models import Item, Application
from user.api.v1.serializers import UserSerializer
from user.models import User


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


class ProfileInfoSerializer(serializers.Serializer):
    profile_id = serializers.IntegerField()


class ProfileInfoOutSerializer(serializers.Serializer):
    comments = ProfileCommentSerializer(read_only=True, many=True)

    class Meta:
        model = Profile
        fields = '__all__'





class UserFriendsSerializer(serializers.Serializer):
    class FriendInfoSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'username',)

    friend = FriendInfoSerializer()


class GetUserInventorySerializer(serializers.Serializer):
    user_id = serializers.IntegerField(min_value=1, max_value=99999999)
    app_id = serializers.IntegerField(min_value=1, max_value=99999999)


class GetOutUserInventorySerializer(serializers.Serializer):

    class InvSerializer(serializers.ModelSerializer):

        class Meta:
            model = Item
            fields = ('name', 'description', 'type', 'quality', 'is_sellable',)

    item = InvSerializer()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)


class AppNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('name',)


class ItemNameSerializer(serializers.ModelSerializer):
    """Serializer to output the item with the item's game name"""

    class Meta:
        model = Item
        fields = ('name', 'application')

    application = AppNameSerializer()


class GetActiveLotsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inventory
        fields = ('price', 'item')

    item = ItemNameSerializer()


class GetSellItemsSerializer(serializers.Serializer):
    item_name = serializers.CharField(required=False)
    app_id = serializers.IntegerField(required=False)
    price_from = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    price_to = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)


class SellingItemOutSerializer(serializers.Serializer):
    class ItemInfoSerializer(serializers.ModelSerializer):
        class Meta:
            model = Item
            fields = ('name', 'type', 'quality', 'application')

        application = AppNameSerializer()

    item = ItemInfoSerializer()
    amount = serializers.IntegerField()
    min_price = serializers.DecimalField(max_digits=10, decimal_places=2)


