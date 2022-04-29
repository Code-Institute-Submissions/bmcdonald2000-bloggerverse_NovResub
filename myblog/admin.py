# django imports
from django.contrib import admin
from .models import Post


# registers my models with the django admin so I can use them.
admin.site.register(Post)
