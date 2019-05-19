from django.db.models import ObjectDoesNotExist
from rest_framework import serializers
from .models import PostCategory, Post
from django.contrib.auth import get_user_model


class CategorySerializer(serializers.ModelSerializer):
    """
    category list
    """

    class Meta:
        model = PostCategory
        fields = ('id', 'category_name', 'category_desc', 'category_link')


class PostAllSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    author_name = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'draft', 'created_at', 'updated_at', 'category', 'author', 'category_name',
                  'author_name')

    def get_category_name(self, obj):
        try:
            category_name = PostCategory.objects.get(pk=obj.category.pk).category_name
        except (TypeError, ObjectDoesNotExist):
            category_name = ''

        return category_name

    def get_author_name(self, obj):
        try:
            User = get_user_model()
            author_name = User.objects.get(pk=obj.author.pk).username
        except (TypeError, ObjectDoesNotExist):
            author_name = ''

        return author_name


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
    author_name = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'draft', 'created_at', 'updated_at', 'category', 'author', 'author_name')

    def get_author_name(self, obj):
        try:
            User = get_user_model()
            author_name = User.objects.get(pk=obj.author.pk).username
        except (TypeError, ObjectDoesNotExist):
            author_name = ''

        return author_name
