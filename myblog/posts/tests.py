from django.contrib.auth import authenticate, login
from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User

from posts.models import *

# Create your tests here.
class PostsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin = User.objects.create_superuser('leejaehyun', 'korea7030@naver.com', 'wogusdlRj1!')
        self.user = User.objects.create_user('user1', 'user1@naver.com', 'wogusdlRj1!')
        self.category = None

    def test_create_category(self):
        """
        create category test
        :return:
        """
        if self.admin.is_superuser:
            self.category = PostCategory(author=self.user, category_name='category1', category_desc='category1 desc')
            category = self.category.save()
            return self.assertTrue(isinstance(category, PostCategory))





