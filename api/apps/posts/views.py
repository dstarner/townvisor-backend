from rest_framework import generics, viewsets
from rest_framework.response import Response

from . import models, serializers


class FeedView(generics.ListAPIView):
    queryset = models.Post.objects.get_latest()
    serializer_class = serializers.PostSerializer


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Post.objects.all()
    lookup_field = 'slug'

    def get_queryset(self):
        if 'user_username' in self.kwargs:
            return self.queryset.filter(author__username=self.kwargs['user_username'])
        return self.queryset

    def get_serializer_class(self):
        if self.detail:
            return serializers.PostDetailSerializer
        return serializers.PostSerializer