from django.urls import path
from rest_framework.routers import DefaultRouter

from user.api.v1.views import UserAPIView

APIMethodsCR = {'get': 'list', 'post': 'create'}
APIMethodsRUD = {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}

urlpatterns = [
    path('user', UserAPIView.as_view(APIMethodsCR)),
    path('user/<int:pk>', UserAPIView.as_view(APIMethodsRUD)),
]
