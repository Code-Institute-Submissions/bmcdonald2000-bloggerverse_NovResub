from django.urls import path
from .views import UserRegView

# URL patters for each page
urlpatterns = [
    path('Register/', UserRegView.as_view(), name='sign_up'),
]
