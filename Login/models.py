from django.db import models
from Blog import settings
from django.contrib.auth.models import User
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class Post(models.Model):
    title = models.CharField(max_length=255)
    thumbails = models.ImageField(editable=True,db_index=True, null=True, blank=True,upload_to="images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    intro = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    editor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='editor')
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return '%s - %s' % (self.post.title, self.editor)