from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from posts import views

urlpatterns = [
    url(r'^$', views.PostCategoryList.as_view(), name='category_list'),
    url(r'^category/(?P<category_pk>[0-9]+)$', views.PostList.as_view(), name='post_list'),
    url(r'^category/(?P<category_pk>[0-9]+)/post/(?P<id>[\w\-]+)/$', views.PostDetail.as_view(), name='post_detail')
]
