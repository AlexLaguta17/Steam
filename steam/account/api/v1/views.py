from django.shortcuts import render
from rest_framework import viewsets, generics, status
from rest_framework.response import Response


from account.models import Profile, Inventory, Friend, Balance, VacBan, ProfileComment, BuyRequest
from games.api.v1.serializers import ItemSerializer
from .serializers import ProfileSerializer, InventorySerializer, FriendSerializer, BalanceSerializer, \
    VacBanSerializer, ProfileCommentSerializer, BuyRequestSerializer, ProfileInfoSerializer, ProfileInfoOutSerializer, \
    UserFriendsSerializer, GetUserInventorySerializer, GetOutUserInventorySerializer, GetActiveLotsSerializer, \
    GetSellItemsSerializer, SellingItemOutSerializer
from ...services.services.inventory import get_user_inventory, get_active_lots, get_selling_items


class ProfileAPIView(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.all()


class InventoryAPIView(viewsets.ModelViewSet):
    serializer_class = InventorySerializer

    def get_queryset(self):
        return Inventory.objects.all()


class FriendAPIView(viewsets.ModelViewSet):
    serializer_class = FriendSerializer

    def get_queryset(self):
        return Friend.objects.all()


class BalanceAPIView(viewsets.ModelViewSet):
    serializer_class = BalanceSerializer

    def get_queryset(self):
        return Balance.objects.all()


class VacBanAPIView(viewsets.ModelViewSet):
    serializer_class = VacBanSerializer

    def get_queryset(self):
        return VacBan.objects.all()


class ProfileCommentAPIView(viewsets.ModelViewSet):
    serializer_class = ProfileCommentSerializer

    def get_queryset(self):
        return ProfileComment.objects.all()


class BuyRequestAPIView(viewsets.ModelViewSet):
    serializer_class = BuyRequestSerializer

    def get_queryset(self):
        return BuyRequest.objects.all()


class GetProfileInfoAPIView(generics.GenericAPIView):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.all()

    def get(self, request, *args, **kwargs):
        profile = self.get_object()
        comment = ProfileComment.objects.filter(profile_id=self.kwargs.get('pk'))
        prof_serializer = ProfileSerializer(profile)
        com_serializer = ProfileCommentSerializer(comment, many=True)
        responce_results = {
            "profile": prof_serializer.data,
            "comments": com_serializer.data
        }
        return Response({'put': responce_results}, status=status.HTTP_200_OK)


class GetUserFriendsAPIView(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        friends = Friend.objects.filter(user_id=self.kwargs.get('user_id'))
        serializer = UserFriendsSerializer(friends, many=True)
        if serializer.data:
            return Response({'get': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'get': "Bad request"}, status=status.HTTP_400_BAD_REQUEST)


class GetUserInventoryAPIView(generics.GenericAPIView):
    serializer_class = GetUserInventorySerializer

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer = GetOutUserInventorySerializer(get_user_inventory(serializer.data), many=True)
        if serializer.data:
            return Response({'put': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'put': "Bad request"}, status=status.HTTP_400_BAD_REQUEST)


class GetActiveLotsAPIView(generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        serializer = GetActiveLotsSerializer(get_active_lots(self.kwargs), many=True)
        if serializer.data:
            return Response({'get': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'get': "Bad request"}, status=status.HTTP_400_BAD_REQUEST)


class GetSellingItemsAPIView(generics.GenericAPIView):
    serializer_class = GetSellItemsSerializer

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer = SellingItemOutSerializer(get_selling_items(serializer.data), many=True)
        if serializer.data:
            return Response({'get': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'get': "Bad request"}, status=status.HTTP_400_BAD_REQUEST)

