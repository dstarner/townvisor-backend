from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        lookup_field = 'username'
        fields = (
            'url',
            'username',
            'email',
            'is_staff',
            'is_mod',
            'first_name',
            'last_name',
        )
        extra_kwargs = {
            'url': {'lookup_field': 'username'}
        }