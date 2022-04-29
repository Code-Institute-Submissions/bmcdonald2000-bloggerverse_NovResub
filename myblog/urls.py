from django.urls import path
from .views import HomeView

# Sets the url pattern for each page.
urlpatterns = [
    path('',  HomeView.as_view(), name="home"),
]
