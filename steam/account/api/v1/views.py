from django.shortcuts import render
from rest_framework import viewsets

from account.models import Profile, Inventory, Friend, Balance, VacBan, ProfileComment, BuyRequest
from .serializers import ProfileSerializer, InventorySerializer, FriendSerializer, BalanceSerializer, \
    VacBanSerializer, ProfileCommentSerializer, BuyRequestSerializer


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
