from rest_framework import serializers

from api.apps.users.serializers import UserSerializer
from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):

    author = UserSerializer()
    replies = serializers.SerializerMethodField()
    user_has_liked = serializers.SerializerMethodField()
    user_has_flagged = serializers.SerializerMethodField()

    def get_user_has_liked(self, comment):
        user = self.context['request'].user
        return comment.likes.filter(creator=user).exists()

    def get_user_has_flagged(self, comment):
        user = self.context['request'].user
        return comment.flags.filter(creator=user).exists()

    class Meta:
        model = Comment
        fields = (
            'id',
            'post',
            'parent',
            'author',
            'replies',
            'content',
            'created',
            'user_has_liked',
            'user_has_flagged',
        )

    def get_replies(self, comment):
        """Return a list of replies for this post
        """
        return CommentSerializer(comment.replies.all(), many=True, context={'request': self.context['request']}).data


class PostSerializer(serializers.HyperlinkedModelSerializer):

    author = UserSerializer()
    header = serializers.ImageField(max_length=None, use_url=True, required=False,)
    thumbnail = serializers.ImageField(max_length=None, use_url=True, required=False,)
    user_has_liked = serializers.SerializerMethodField()
    user_has_flagged = serializers.SerializerMethodField()

    def get_user_has_liked(self, post):
        user = self.context['request'].user
        return post.likes.filter(creator=user).exists()

    def get_user_has_flagged(self, comment):
        user = self.context['request'].user
        return comment.flags.filter(creator=user).exists()

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
            'number_of_likes',
            'is_flagged',
            'user_has_liked',
            'user_has_flagged',
        )
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }
        write_only_fields = (
            'md_content',
        )
        read_only_fields = (
            'slug',
        )

class PostDetailSerializer(PostSerializer):
    """Provides a more detailed view of a post
    """
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
        read_only_fields = PostSerializer.Meta.read_only_fields
