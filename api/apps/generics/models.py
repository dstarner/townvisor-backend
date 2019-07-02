from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django_extensions.db.fields import CreationDateTimeField


class Like(models.Model):

    creator = models.ForeignKey(
        get_user_model(),
        help_text='Who is doing the liking',
        on_delete=models.CASCADE,
        related_name='likes',
    )
    timestamp = CreationDateTimeField()

    # What is being liked
    limit = models.Q(app_label = 'posts')
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to=limit
    )
    object_id = models.CharField(max_length=64)
    content_object = GenericForeignKey()

    def __str__(self):
        return f'Like by {str(self.creator)}'

    class Meta:
        db_table = 'likes'
        ordering = ['-timestamp']
        verbose_name = 'Like'
        verbose_name_plural = 'Likes'


class Flag(models.Model):

    creator = models.ForeignKey(
        get_user_model(),
        help_text='Who performed the flag',
        on_delete=models.CASCADE,
        related_name='flags',
    )
    timestamp = CreationDateTimeField()

    # What is being flagged
    limit = models.Q(app_label = 'posts') | models.Q(app_label = 'users')
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        limit_choices_to=limit
    )
    object_id = models.CharField(max_length=64)
    content_object = GenericForeignKey()

    def __str__(self):
        return f'Like by {str(self.creator)}'

    class Meta:
        db_table = 'flags'
        ordering = ['-timestamp']
        verbose_name = 'Flag'
        verbose_name_plural = 'Flags'