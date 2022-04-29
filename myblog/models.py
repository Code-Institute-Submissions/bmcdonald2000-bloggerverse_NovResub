# django imports, packages and components
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# fields and behaviours for Post model
class Post(models.Model):
    title = models.CharField(max_length=255)
    # RichTextField gives user all the tool style their post
    body = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    summary = models.CharField(max_length=255)

    # function for admin page to view post title and author
    def __str__(self):
        return self.title + ' | ' + str(self.author)
