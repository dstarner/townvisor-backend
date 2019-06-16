from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'author', 'published', 'created', 'last_modified')

    list_filter = ('published', )

    read_only = ('slug',)

    search_fields = ('title', 'author__username',)

admin.site.register(Post, PostAdmin)

