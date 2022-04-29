# django imports
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic import DetailView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Post, comment, Category
from .forms import PostForms, EditForm, CommentForm


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


# displays delte post page using django DeleteView
class DeletePostView(SuccessMessageMixin, DeleteView):

    # using Post model
    model = Post

    # using html template to display delete post page
    template_name = 'delete.html'

    # if post is deleted user is returned the homepage
    success_url = reverse_lazy('home')

    # adds a message if the form is success using SuccessMessageMixin
    success_message = " Your post was deleted from the Bloggerverse "


# displays comments page using django CreateView
class CommentView(SuccessMessageMixin, CreateView):

    # using comment model
    model = comment

    # using CommentForm
    form_class = CommentForm

    # using html template to display comments
    template_name = 'comment.html'

    # adds a message if the form is success using SuccessMessageMixin
    success_message = " Thanks for sharing your thoughts in the Bloggerverse"


# displays add category page using django CreateView
class AddCategoryView(SuccessMessageMixin, CreateView):

    # using Category model
    model = Category

    # using html template to display add category page
    template_name = 'categories.html'

    # using all the fields
    fields = '__all__'

    # redirects user to the post form if form successful
    success_url = reverse_lazy('posts')

    # adds a message if the form is successful using SuccessMessageMixin
    success_message = " We have added your category to the Bloggerverse"