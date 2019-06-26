from django.contrib.auth import get_user_model
from django.db import models
from django_extensions.db.fields import (
    AutoSlugField, CreationDateTimeField, ModificationDateTimeField, RandomCharField
)

from api.config.storage_backends import PrivateMediaStorage


class PostManager(models.Manager):
    
    def get_latest(self):
        return self.get_queryset().order_by('-created')


class Post(models.Model):

    title = models.CharField(
        blank=False,
        null=False,
        max_length=128,
    )

    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='posts',
    )

    slug = AutoSlugField(
        primary_key=True,
        unique=True,
        populate_from=['title'],
        help_text='Unique UUID string that represents the post',
    )

    published = models.BooleanField(default=False, help_text='Is the post published and public')

    created = CreationDateTimeField(verbose_name='Creation Time')

    last_modified = ModificationDateTimeField(verbose_name='Last Modified Time')

    thumbnail = models.ImageField(
        storage=PrivateMediaStorage(),
        blank=True,
        null=True
    )

    header = models.ImageField(
        storage=PrivateMediaStorage(),
        blank=True,
        null=True
    )
    header_caption = models.CharField(max_length=128, default='', blank=True, null=True)

    md_content = models.TextField(
        default='',
        verbose_name='Markdown Content',
        help_text='Markdown content for the blog post'
    )

    objects = PostManager()

    def __str__(self):
        return self.title

    def abs_path(self):
        return f'{self.author.profile_url}/{self.slug}'

    class Meta:
        db_table = 'posts'
        ordering = ['-created']


class Comment(models.Model):

    id = RandomCharField(primary_key=True, editable=False, length=15, unique=True)

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)

    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name='replies', null=True, blank=True)

    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='comments',
    )

    content = models.TextField(default='')

    created = CreationDateTimeField(verbose_name='Creation Time')

    class Meta:
        db_table = 'comments'
        ordering = ['-created']

    def __str__(self):
        return f'Comment #{self.id}'

    @property
    def post_name(self):
        """Get the name of the post its attached to
        """
        if self.post is not None:
            return self.post.title
        return self.parent.post_name