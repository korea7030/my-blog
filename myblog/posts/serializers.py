from rest_framework import serializers
from .models import PostCategory, Post


class PostCategorySerializer(serializers.ModelSerializer):
    """
    blog category list
    """

    class Meta:
        model = PostCategory
        fields = ('id', 'category_name', 'category_desc',)

    def to_representation(self, data):
        category = data.__class__.objects.get(id=self.context['category_pk'])
        return super(PostCategorySerializer, self).to_representation(category)


class PostSerializer(serializers.ModelSerializer):
    """
    blog post by category
    """
    category = PostCategorySerializer(many=False, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'draft', 'created_at', 'updated_at', 'category')


class PostDetailSerializer(serializers.ModelSerializer):
    """
    post detail
    """

    category = PostCategorySerializer(many=False, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'draft', 'created_at', 'updated_at', 'category')
