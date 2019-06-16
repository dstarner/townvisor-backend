from rest_framework import serializers

from api.apps.users.serializers import UserSerializer
from .models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):

    author = UserSerializer()

    class Meta:
        model = Post
        fields = (
            'url',
            'title',
            'author',
            'created',
            'last_modified',
            'slug',
        )
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

class PostDetailSerializer(serializers.HyperlinkedModelSerializer):

    author = UserSerializer()

    class Meta:
        model = Post
        lookup_field = 'slug'
        fields = (
            'url',
            'title',
            'author',
            'created',
            'last_modified',
            'slug',
            'md_content',
        )
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }