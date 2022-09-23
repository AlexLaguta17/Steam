from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

from games.models import Application, Library, Item, GameComment
from .serializers import ApplicationSerializer, LibrarySerializer, ItemSerializer, GameCommentSerializer
from rest_framework import viewsets


class ApplicationAPIView(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Application.objects.all()


class LibraryAPIView(viewsets.ModelViewSet):
    serializer_class = LibrarySerializer

    def get_queryset(self):
        return Library.objects.all()


class ItemAPIView(viewsets.ModelViewSet):
    serializer_class = ItemSerializer

    def get_queryset(self):
        return Item.objects.all()


class GameCommentAPIView(viewsets.ModelViewSet):
    serializer_class = GameCommentSerializer

    def get_queryset(self):
        return GameComment.objects.all()
