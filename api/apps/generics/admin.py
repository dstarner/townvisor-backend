from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

from .models import Like


class LikesInline(GenericStackedInline):
    model = Like
    readonly_fields = ('timestamp', )
    autocomplete_fields = ('creator',)
    extra = 0