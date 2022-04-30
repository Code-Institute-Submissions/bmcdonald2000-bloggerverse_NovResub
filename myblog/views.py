# django imports
from users.models import Post, comment, Category
from users.forms import PostForms, EditForm, CommentForm
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic import DetailView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


# displays blog posts on the home page in a list
class HomeView(ListView):

    # using Post model
    model = Post

    # using html template to display blog post on the home page
    template_name = 'home.html'

    # post apprear in date order (recent first)
    ordering = ['-date']

    # post category is visible on the home page
    category = Category.objects.all()

    # displays the categories used in the dropdown menu
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["category_menu"] = category_menu
        return context


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

    # displays the categories used in the dropdown menu
    def get_context_data(self, *args, **kwargs):
        category_menu = Category.objects.all()
        context = super(postView, self).get_context_data(*args, **kwargs)

        # displays the number of likes a post has
        x = get_object_or_404(Post, id=self.kwargs['pk'])
        num_likes = x.num_likes()

        # stops the user from liking the same post twice
        liked = False
        if x.like.filter(id=self.request.user.id).exists():
            liked = True

        context["category_menu"] = category_menu
        context["num_likes"] = num_likes
        context["liked"] = liked
        return context


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


# function to display the hyperlinked categories on the category page
def CategoryListView(request):
    category_list = Category.objects.all()
    return render(request, 'category_list.html',
                  {'category_list': category_list})


# function to slugify category page
def CategoryView(request, category):
    post_category = Post.objects.filter(category=category.replace('-', ' '))
    return render(request, 'category_pages.html',
                  {'category': category.replace('-', ' ').title(),
                   'post_category': post_category})


# function to show post likes
def LikePostView(request, pk):

    # when a post is liked, the post id will be saved to the database.
    liked_post = get_object_or_404(Post, id=request.POST.get('like_id'))
    liked = False

    # like button changes to dislike after it has been liked
    if liked_post.like.filter(id=request.user.id).exists():
        liked_post.like.remove(request.user)
        liked = False
    else:
        liked_post.like.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('details', args=[str(pk)]))
