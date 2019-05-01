from rest_framework import generics
from rest_framework.response import Response

from .models import PostCategory, Post
from .serializers import PostCategorySerializer, PostSerializer, PostDetailSerializer


# Create your views here.
class PostCategoryList(generics.ListAPIView):
    """
    category list view
    """
    queryset = PostCategory.objects.all()
    serializer_class = PostCategorySerializer


class PostList(generics.ListAPIView):
    """
    post list by category view
    notice: if pass a queryset to serializer, many=True
            if pass a single model object(use get), many=False)
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

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
