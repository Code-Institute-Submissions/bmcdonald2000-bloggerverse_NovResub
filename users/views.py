# django imports
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegForm
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
