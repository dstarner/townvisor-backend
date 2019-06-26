from rest_framework import generics, viewsets
from rest_framework.response import Response

from . import models, serializers


class FeedView(generics.ListAPIView):
    queryset = models.Post.objects.get_latest()
    serializer_class = serializers.PostSerializer


class PostViewSet(viewsets.ModelViewSet):
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


class CommentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Comment.objects.all()
    page_size = 10

    def get_queryset(self):
        if 'post_slug' in self.kwargs:
            return self.queryset.filter(post__slug=self.kwargs['post_slug'])
        if 'user_slug' in self.kwargs:
            return self.queryset.filter(author__slug=self.kwargs['user_slug'])
        if 'parent_id' in self.kwargs:
            return self.queryset.filter(parent__id=self.kwargs['parent_id'])
        return self.queryset

    def get_serializer_class(self):
        if self.detail:
            return serializers.CommentSerializer
        return serializers.CommentSerializer