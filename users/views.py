# django imports
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from .forms import RegForm, ProfilePageForm
from myblog.models import UserProfile
from django.contrib.messages.views import SuccessMessageMixin


# displays user regitstration page using django CreateView
class UserRegView(SuccessMessageMixin, CreateView):
    # using RegForm
    form_class = RegForm

    # displayed on html template page
    template_name = 'registration/sign_up.html'

    # adds a message if the form is success using SuccessMessageMixin
    success_message = " Welcome to the Bloggerverse !"

    # if form is completly successfully then user is returned to the login page
    success_url = reverse_lazy('home')


# displays create profile page using django CreateView
class create_profile_view(SuccessMessageMixin, CreateView):

    # using UserProfile model
    model = UserProfile

    # using ProfilePageForm
    form_class = ProfilePageForm

    # displayed on html template page
    template_name = 'registration/create_profile.html'

    # adds a message if the form is success using SuccessMessageMixin
    success_message = " Now you're 100% ready to enter the Bloggerverse"

    # The user id is used to save the form under the user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# displays view profile page using django DetailView
class ProfilePageView(DetailView):

    # using UserProfile model
    model = UserProfile

    # displayed on html template page
    template_name = 'registration/view_profile.html'
