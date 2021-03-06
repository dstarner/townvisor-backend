from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.contrib.auth.validators import UnicodeUsernameValidator

from api.config.storage_backends import PrivateMediaStorage


class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email), **kwargs)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        kwargs['is_staff'] = True
        kwargs['is_superuser'] = True
        user = self.create_user(
            email,
            password=password,
            **kwargs,
        )
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        max_length=150,
        unique=True,
        primary_key=True,
        help_text='Unique username to identify the user. Letters, digits and @/./+/-/_ only.',
        validators=[username_validator],
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    # PERSONAL INFORMATION

    first_name = models.CharField(max_length=255, default='')

    last_name = models.CharField(max_length=255, default='')

    date_of_birth = models.DateField(verbose_name='Date of Birth', help_text='In YYYY-MM-DD format')

    about = models.TextField(
        default='I haven\'t filled my About section out yet!',
        help_text='Profile description for the user',
    )

    avatar = models.ImageField(
        storage=PrivateMediaStorage(),
        blank=True,
        null=True
    )

    header = models.ImageField(
        storage=PrivateMediaStorage(),
        help_text='The header image can be used as a backsplash for the user\'s profile.',
        blank=True,
        null=True
    )

    # PERMISSIONS

    is_active = models.BooleanField(default=True, verbose_name='Active Status')

    is_staff = models.BooleanField(
        default=False,
        verbose_name='Staff Status',
        help_text='Designates that this user can log into the admin site.'
    )

    is_mod = models.BooleanField(
        default=False,
        verbose_name='Moderator Status',
        help_text='Designates that this user has extra power to flag, report, and ban users / posts.'
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'date_of_birth']


    def __str__(self):
        return self.username

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def profile_url(self):
        return f'/{self.username}'