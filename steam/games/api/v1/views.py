from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

from games.models import Application, Library, Item, GameComment
from .serializers import ApplicationSerializer, LibrarySerializer, ItemSerializer, GameCommentSerializer, \
    GetInApplicationInfoSerializer, GetOutApplicationInfoSerializer, GetInUserAppInfoSerializer, \
    GetOutUserAppInfoSerializer, GetOutTopAppsSerializer
from rest_framework import viewsets, generics, status
from rest_framework.response import Response


from ...services.services.get_app import get_app
from ...services.services.get_user_apps import get_user_apps, get_top_user_apps


class ApplicationAPIView(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    #permission_classes = (IsAuthenticated,)

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


class GetApplicationInfoAPIView(generics.GenericAPIView):
    serializer_class = GetInApplicationInfoSerializer

    def get_queryset(self):
        return Application.objects.all()

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        filtered_apps = get_app(serializer.validated_data)
        serializer = GetOutApplicationInfoSerializer(filtered_apps, many=True)
        if serializer.data:
            return Response({'put': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'put': "Bad request"}, status=status.HTTP_400_BAD_REQUEST)


class GetUserAppAPIView(generics.GenericAPIView):
    serializer_class = GetInUserAppInfoSerializer

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer = GetOutUserAppInfoSerializer(get_user_apps(serializer.validated_data), many=True)
        if serializer.data:
            return Response({'put': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'put': "Bad request"}, status=status.HTTP_400_BAD_REQUEST)


class GetTopUserAppsAPIView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        serializer = GetOutTopAppsSerializer(get_top_user_apps(self.kwargs.get('pk')), many=True)
        if serializer.data:
            return Response({'get': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'get': "Bad request"}, status=status.HTTP_400_BAD_REQUEST)
