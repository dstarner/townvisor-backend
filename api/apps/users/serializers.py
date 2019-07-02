from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):

    avatar = serializers.ImageField(
        max_length=None,
        use_url=True,
        required=False,
        read_only=True,
    )
    header = serializers.ImageField(
        max_length=None,
        use_url=True,
        required=False,
        read_only=True,
    )

    first_name = serializers.CharField(
        required=True,
    )

    last_name = serializers.CharField(
        required=True,
    )

    user_has_flagged = serializers.SerializerMethodField()

    def get_user_has_flagged(self, comment):
        user = self.context['request'].user
        return comment.flags.filter(creator=user).exists()

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
            'date_of_birth',
            'user_has_flagged',
        )
        extra_kwargs = {
            'url': {'lookup_field': 'username'}
        }
        write_only_fields = (
            'date_of_birth',
        )
        read_only_fields = (
            'is_staff',
            'is_mod',
            'avatar',
            'header',
        )


class ChangePasswordSerializer(serializers.Serializer):

    current_password = serializers.CharField(required=True, help_text='Current password for the user')

    new_password = serializers.CharField(required=True, help_text='New password for the user')