# django imports
from django import forms
from .models import Post, comment, Category

# options = [('law', 'law'), ('coding', 'coding')]
# creates a query of names from the Category model
options = Category.objects.all().values_list('name', 'name')

# creates a categories lists
categories_list = []

# any new items are added to the list
for item in options:
    categories_list.append(item)


# creates a form for the posts using a model
class PostForms(forms.ModelForm):

    # form metadata options
    class Meta:
        # using Post model
        model = Post
        # fields that will be used for the form
        fields = ('title', 'author', 'image', 'body', 'category', 'summary')

        # basic controls/styling for the form fields
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder':
                                            'Enter post title'}),
            'author': forms.TextInput(attrs={'value': '', 'id': 'username',
                                             'type': 'hidden'}),
            'category': forms.Select(choices=options,
                                     attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'summary': forms.Textarea(attrs={'class': 'form-control'}),
        }


# creates an edit form using  a model
class EditForm(forms.ModelForm):

    # form metadata options
    class Meta:
        # using Post model
        model = Post

        # fields that will be used for the form
        fields = ('title', 'body', 'summary')

        # basic controls/styling for the form fields
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder':
                                            'Enter Post Title'}),
            'body': forms.Textarea(attrs={'class': 'form-control',
                                          'placeholder':
                                          'Type your Post'}),
            'summary': forms.Textarea(attrs={'class': 'form-control',
                                             'placeholder':
                                             'Summarise your post'}),
        }


# creates a comment form using a model
class CommentForm(forms.ModelForm):

    # form metadata options
    class Meta:
        # using comment model
        model = comment

        # fields that will be used for the form
        fields = ('name', 'body')

        # basic controls/styling for the form fields
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', }),
            'body': forms.Textarea(attrs={'class': 'form-control',
                                          'placeholder': 'Enter comment'}),
        }
