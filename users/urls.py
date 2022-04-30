from django.urls import path
from .views import UserRegView, create_profile_view, ProfilePageView
from .views import EditProfileSettingsView
from .views import EditProfileView

# URL patters for each page
urlpatterns = [
    path('Register/', UserRegView.as_view(), name='sign_up'),
    path('create_profile/', create_profile_view.as_view(),
         name='create_profile'),
    path('<int:pk>/Profile/', ProfilePageView.as_view(),
         name='view_profile'),
    path('<int:pk>/Edit_profile/', EditProfileView.as_view(),
         name='profile'),
    path('Edit_settings/', EditProfileSettingsView.as_view(),
         name='profile_settings'),
]
