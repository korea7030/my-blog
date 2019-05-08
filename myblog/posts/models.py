from django.conf import settings
from django.core.urlresolvers import reverse
from markdownx.models import MarkdownxField
from django.utils.safestring import mark_safe
from markdown_deux import markdown

from common.models import *


# Create your models here.
def upload_location(instance, filename):
    # filebase, extension = filename.split(".")
    # return "%s/%s.%s" %(instance.id, instance.id, extension)
    PostModel = instance.__class__  # get the model Post.
    new_id = PostModel.objects.order_by("id").last().id + 1
    return "%s/%s" % (new_id, filename)


class PostCategory(AbstractCreateUpdateModel):
    """
    category information (deeplearning, blockchain...)
    """
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    category_name = models.CharField(max_length=120)
    category_desc = models.CharField(max_length=1000)
    category_link = models.CharField(max_length=100)

    class Meta:
        db_table = 'post_category'

    def __str__(self):
        return self.category_name


class Post(AbstractCreateUpdateModel):
    """
    blog post information
    """
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE, related_name='post_category')
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=120)
    content = MarkdownxField()
    draft = models.BooleanField(default=False)
    # read_time = models.TimeField(null=True, blank=True)

    class Meta:
        db_table = 'post'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"id": self.id})

    def get_markdown(self):
        content = self.content
        markdown_text = markdown(content)
        return mark_safe(markdown_text)
