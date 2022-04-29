# django imports
from .models import Post
from django.views.generic import ListView


# displays blog posts on the home page in a list
class HomeView(ListView):

    # using Post model
    model = Post

    # using html template to display blog post on the home page
    template_name = 'home.html'
