from django.contrib import admin
from django import forms

from .models import Post, Comment


class CommentAdminForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = '__all__'

    def clean_parent(self):
        """Check that it doesnt refer to itself, and that theres no reply loop
        """
        parent = self.cleaned_data['parent']
        if parent is None:
            return parent

        if parent.id == self.instance.id:
            raise forms.ValidationError("Comment cannot be it's reply")
        
        checked_comment = parent
        while checked_comment is not None:
            throw = False
            if checked_comment.id == self.instance.id:
                throw = True
            if checked_comment.parent and checked_comment.parent.id == self.instance.id:
                throw = True
            if throw:
                raise forms.ValidationError(f'{parent} is already a reply to this comment, cannot create loop')
            checked_comment = checked_comment.parent            
        return parent

    def clean(self):
        """A Comment should not be attached to a post and a comment
        """
        cleaned_data = super().clean()
        parent = cleaned_data.get('parent', None)
        post = cleaned_data.get('post', None)
        if post and parent:
            raise forms.ValidationError('Cannot have post a post and a comment as a parent. If a nested comment, please set post to null')


class CommentInline(admin.StackedInline):

    model = Comment
    extra = 0


class CommentAdmin(admin.ModelAdmin):

    form = CommentAdminForm

    list_display = ('post_name', 'author', 'id', 'created', 'parent')

    search_fields = ('id', 'post__title', 'parent__post__title')

    readonly_fields = ('created',)


class PostAdmin(admin.ModelAdmin):

    list_display = ('title', 'slug', 'author', 'published', 'created', 'last_modified')

    list_filter = ('published', )

    inlines = (CommentInline,)

    readonly_fields = ('slug',)

    search_fields = ('title', 'author__username',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)

