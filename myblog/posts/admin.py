from django.db import models
from django.contrib import admin
from django.template.defaultfilters import truncatechars
from markdownx.admin import MarkdownxModelAdmin
from posts.models import PostCategory, Post
from martor.widgets import AdminMartorWidget


class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'category_desc', 'author', 'category_link']


class PostAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'get_content', 'draft', 'created_at', 'updated_at']
    # link anchor show
    list_display_links = ['category', 'title']
    # filter
    list_filter = ('title', 'category')
    # search word
    search_fields = ['category', 'title', 'content']


    def get_content(self, obj):
        return truncatechars(obj.content, 100)

    get_content.short_description = 'content'

# Register your models here.
admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Post, PostAdmin)
