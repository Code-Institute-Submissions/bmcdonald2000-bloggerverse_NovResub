# django imports
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic import DetailView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Post
from .forms import PostForms, EditForm


# displays blog posts on the home page in a list
class HomeView(ListView):

    # using Post model
    model = Post

    # using html template to display blog post on the home page
    template_name = 'home.html'


# displays add post page using django CreateView
class AddPostView(SuccessMessageMixin, CreateView):

    # using Post model
    model = Post

    # using pForms
    form_class = PostForms

    # using html template to display add post page
    template_name = 'posts.html'

    # adds a message if the form is success using SuccessMessageMixin
    success_message = " Thank you for adding your post to the Bloggerverse"


# displays view post page using django DetailView
class postView(DetailView):

    # using Post model
    model = Post

    # using html template to display post
    template_name = 'post_details.html'


# displays edit post page using django UpdateView
class EditPostView(SuccessMessageMixin, UpdateView):

    # using Post model
    model = Post

    # using EditForm
    form_class = EditForm

    # using html template to display edit post page
    template_name = 'edit.html'

    # adds a message if the form is success using SuccessMessageMixin
    success_message = " Awesome !! your blog has been updated "
