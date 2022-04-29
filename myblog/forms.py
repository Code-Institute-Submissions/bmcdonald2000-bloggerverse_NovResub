# django imports
from django import forms
from .models import Post


# creates a form for the posts using a model
class PostForms(forms.ModelForm):

    # form metadata options
    class Meta:
        # using Post model
        model = Post
        # fields that will be used for the form
        fields = ('title', 'author', 'body', 'summary')

        # basic controls/styling for the form fields
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder':
                                            'Enter post title'}),
            'author': forms.TextInput(attrs={'value': '', 'id': 'username',
                                             'type': 'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'summary': forms.Textarea(attrs={'class': 'form-control'}),
        }
