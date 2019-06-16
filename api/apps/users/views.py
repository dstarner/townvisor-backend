from rest_framework import viewsets

from . import models, serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    lookup_field = 'username'

    def get_serializer_class(self):
        return serializers.UserSerializer
