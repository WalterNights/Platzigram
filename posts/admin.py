#Post Classes

#Django
from django.contrib import admin

#Post
from posts.models import Post
from django.contrib.auth.models import User

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post Admin"""
    list_display = (
        'pk', 
        'user', 
        'title', 
        'photo'
    )
    list_display_links = (
        'pk', 
        'user'
    )
    list_editable = (
        'title', 
        'photo'
    )
    search_fields = (
        'user__username', 
        'title'
    )
    list_filter = (
        'created', 
        'modified'
    )
    readonly_fields = (
        'created', 
        'modified'
    )
