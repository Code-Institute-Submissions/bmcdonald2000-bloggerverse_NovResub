# django imports, packages and components
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from datetime import date


# fields and behaviours for Post model
class Post(models.Model):
    title = models.CharField(max_length=255)
    # RichTextField gives user all the tool style their post
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    body = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    summary = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True,
                            default=date.today)

    # function for admin page to view post title and author
    def __str__(self):
        return self.title + ' | ' + str(self.author)

    # function to redirect user to view the post they just made
    def get_absolute_url(self):
        return reverse('details', args=[str(self.id)])
