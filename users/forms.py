# django imports
from myblog.models import UserProfile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
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


# creates profile form using django models
class ProfilePageForm(forms.ModelForm):
    # form metadata options
    class Meta:

        model = UserProfile

        fields = ('Bio', 'profile_picture',
                  'Website', 'Youtube', 'Twitter',
                  'Instagram', 'Podcast', 'Linkedin')

        # adds basic style/controls to widget instances
        widgets = {
            'Bio': forms.Textarea(attrs={'class': 'form-control'}),
            'Website': forms.TextInput(attrs={'class':
                                              'form-control', 'placeholder':
                                                              "Website URL"}),
            'Youtube': forms.TextInput(attrs={'class':
                                              'form-control', 'placeholder':
                                                              "Youtube URL"}),
            'Podcast': forms.TextInput(attrs={'class':
                                              'form-control', 'placeholder':
                                                              "Podcast URL"}),
            'Twitter': forms.TextInput(attrs={'class':
                                              'form-control', 'placeholder':
                                                              "Twitter URL"}),
            'Instagram': forms.TextInput(attrs={'class':
                                                'form-control',
                                                'placeholder':
                                                "Instagram URL"}),
            'Linkedin': forms.TextInput(attrs={'class':
                                               'form-control',
                                               'placeholder':
                                               "Linkedin URL"}),
            }


# form uses django UserChange so users can change their profile settings
class ProfileSettingsForm(UserChangeForm):
    # sets basic style/controls for each form field
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':
                                                            'form-control'}))
    first_name = forms.CharField(max_length=100,
                                 widget=forms.TextInput(
                                        attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100,
                                widget=forms.TextInput(
                                        attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100,
                               widget=forms.TextInput(
                                        attrs={'class': 'form-control'}))
    last_login = forms.CharField(max_length=100,
                                 widget=forms.TextInput(
                                        attrs={'class': 'form-control'}))
    is_superuser = forms.CharField(max_length=100,
                                   widget=forms.CheckboxInput(
                                        attrs={'class': 'form-check',
                                               'type': 'hidden'}))
    is_staff = forms.CharField(max_length=100,
                               widget=forms.CheckboxInput(
                                        attrs={'class': 'form-check',
                                               'type': 'hidden'}))
    is_active = forms.CharField(max_length=100,
                                widget=forms.CheckboxInput(
                                        attrs={'class': 'form-check',
                                               'type': 'hidden'}))
    date_joined = forms.CharField(max_length=100,
                                  widget=forms.TextInput(
                                        attrs={'class': 'form-control',
                                               'type': 'hidden'}))

    # form metadata options
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',
                  'password', 'last_login', 'is_superuser', 'is_staff',
                  'is_active', 'date_joined')


# change password form is built using django PasswordChangeForm
class ChangePasswordForm(PasswordChangeForm):

    old_password = forms.CharField(
                         widget=forms.PasswordInput(
                                      attrs={'class': 'form-control',
                                             'type': 'password'}))
    new_password1 = forms.CharField(max_length=100,
                                    widget=forms.PasswordInput(
                                                 attrs={'class':
                                                        'form-control',
                                                        'type':
                                                        'password'}))
    new_password2 = forms.CharField(max_length=100,
                                    widget=forms.PasswordInput(
                                                 attrs={'class':
                                                        'form-control',
                                                        'type': 'password'}))

    # form metadata options
    class Meta:

        model = User
        fields = ('old_password', 'new_password1', 'new_password2'),
