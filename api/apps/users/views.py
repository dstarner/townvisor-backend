from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from . import models, serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    lookup_field = 'username'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    @action(
        detail=False,
        url_path='change-password',
        methods=['post'],
        permission_classes=[permissions.IsAuthenticated],
        serializer_class=serializers.ChangePasswordSerializer,
    )
    def change_password(self, request):
        """Change the existing user's password
        """

        return Response({'hello': 'world'})

    def get_serializer_class(self):
        if self.action == 'change_password':
            return serializers.ChangePasswordSerializer
        return serializers.UserSerializer
