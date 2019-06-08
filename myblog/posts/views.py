from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import PostCategory, Post
from .serializers import (CategorySerializer,
                          PostSerializer,
                          PostAllSerializer,
                          PostDetailSerializer)


# Create your views here.
class PostCategoryList(generics.ListAPIView):
    """
    category list view
    """
    queryset = PostCategory.objects.all().order_by('-created_at')
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)


class PostAllList(generics.ListAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostAllSerializer
    permission_classes = (AllowAny,)


class PostList(generics.ListAPIView):
    """
    post list by category view
    notice: if pass a queryset to serializer, many=True
            if pass a single model object(use get), many=False)
    """
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = self.queryset.filter(category__pk=self.kwargs['category_pk'])
        return queryset

    def get_serializer(self, *args, **kwargs):
        """
        serializer 정보를 가져와 parameter 전달
        :param args: parameter1
        :param kwargs: parameter2
        :rtype: serializer object
        """
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def get_serializer_context(self):
        """
        전달받은 값을 반환
        :rtype: dict
        """
        return {
            'category_pk': self.kwargs['category_pk']
        }


class PostDetail(generics.RetrieveAPIView):
    lookup_field = "id"
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = (AllowAny,)

    def get_serializer(self, *args, **kwargs):
        """
        serializer 정보를 가져와 parameter 전달
        :param args: parameter1
        :param kwargs: parameter2
        :rtype: serializer object
        """
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def get_serializer_context(self):
        """
        전달받은 값을 반환
        :rtype: dict
        """
        return {
            'category_pk': self.kwargs['category_pk']
        }
