from django.urls import path
from .views import HomeView, AddPostView

# Sets the url pattern for each page.
urlpatterns = [
    path('',  HomeView.as_view(), name="home"),
    path('Add_Post/', AddPostView.as_view(), name='posts'),
]
