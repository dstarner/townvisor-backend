from django.contrib.auth import get_user_model
from django.db import models
from django_extensions.db.fields import (
    AutoSlugField, CreationDateTimeField, ModificationDateTimeField
)


class PostManager(models.Manager):
    
    def get_latest(self):
        return self.get_queryset().order_by('-created')


class Post(models.Model):

    title = models.CharField(default='', max_length=128)

    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='posts',
    )

    slug = AutoSlugField(populate_from=['title'])

    published = models.BooleanField(default=False, help_text='Is the post published and public')

    created = CreationDateTimeField(verbose_name='Creation Time')

    last_modified = ModificationDateTimeField(verbose_name='Last Modified Time')

    md_content = models.TextField(
        default='',
        verbose_name='Markdown Content',
        help_text='Markdown content for the blog post'
    )

    objects = PostManager()

    def __str__(self):
        return self.title

