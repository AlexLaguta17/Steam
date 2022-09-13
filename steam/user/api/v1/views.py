from rest_framework import viewsets

from user.api.v1.serializers import UserSerializer
from user.models import User


class UserAPIView(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()
