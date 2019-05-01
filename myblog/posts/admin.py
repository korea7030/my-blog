from django.contrib import admin
from posts.models import PostCategory, Post


class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name', 'category_desc', 'author']


class PostAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'content', 'draft', 'created_at', 'updated_at']
    # link anchor show
    list_display_links = ['category', 'title']
    # filter
    list_filter = ('title', 'category')
    # search word
    search_fields = ['category', 'title', 'content']


# Register your models here.
admin.site.register(PostCategory, PostCategoryAdmin)
admin.site.register(Post, PostAdmin)
