from rest_framework import serializers

from api.apps.users.serializers import UserSerializer
from .models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):

    author = UserSerializer()
    header = serializers.ImageField(max_length=None, use_url=True)
    thumbnail = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Post
        fields = (
            'url',
            'title',
            'author',
            'created',
            'last_modified',
            'slug',
            'header',
            'thumbnail',
            'abs_path',
        )
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }

class PostDetailSerializer(serializers.HyperlinkedModelSerializer):

    author = UserSerializer()
    header = serializers.ImageField(max_length=None, use_url=True)
    thumbnail = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Post
        lookup_field = 'slug'
        fields = PostSerializer.Meta.fields + (
            'header_caption',
            'md_content',
        )
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }