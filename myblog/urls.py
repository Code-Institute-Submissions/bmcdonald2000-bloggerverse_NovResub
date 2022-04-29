from django.urls import path
from .views import HomeView, postView, AddPostView, EditPostView

# Sets the url pattern for each page.
urlpatterns = [
    path('',  HomeView.as_view(), name="home"),
    path('Posts/<int:pk>/', postView.as_view(), name='details'),
    path('Add_Post/', AddPostView.as_view(), name='posts'),
    path('Posts/Edit/<int:pk>', EditPostView.as_view(), name='edit'),
]
