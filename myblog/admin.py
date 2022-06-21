# django imports
from django.contrib import admin
from .models import Post, Category, comment, UserProfile


# registers my models with the django admin so I can use them.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(comment)
admin.site.register(UserProfile)
