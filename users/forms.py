# django imports
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import forms


# creates django form using django UserCreationForm
class RegForm(UserCreationForm):

    # sets controls/styling for form fields
    email = forms.EmailField(widget=forms.EmailInput(attrs={
                                                    'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
                                                    'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
                                                    'class': 'form-control'}))

    # form metadata options
    class Meta:

        # using User model
        model = User

        # fields that will be used for the form
        fields = ('username', 'first_name', 'last_name', 'email',
                  'password1', 'password2')

    # basic style/controls to the form fields not listed in the class
    def __init__(self, *args, **kwargs):
        super(RegForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
