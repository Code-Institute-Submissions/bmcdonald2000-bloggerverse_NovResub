from django.urls import path
from views import UserRegView, create_profile_view

# URL patters for each page
urlpatterns = [
    path('Register/', UserRegView.as_view(), name='sign_up'),
    path('create_profile/', create_profile_view.as_view(),
         name='create_profile'),
]
