from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):

    avatar = serializers.ImageField(max_length=None, use_url=True)
    header = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = get_user_model()
        lookup_field = 'username'
        fields = (
            'url',
            'about',
            'avatar',
            'header',
            'profile_url',
            'username',
            'email',
            'is_staff',
            'is_mod',
            'first_name',
            'last_name',
            'full_name',
        )
        extra_kwargs = {
            'url': {'lookup_field': 'username'}
        }