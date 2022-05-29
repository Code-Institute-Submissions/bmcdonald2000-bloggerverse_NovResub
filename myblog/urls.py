from django.urls import path
from .views import HomeView, PostView, AddPostView
from .views import EditPostView, DeletePostView
from .views import CommentView, AddCategoryView
from .views import CategoryListView, CategoryView
from .views import LikePostView



# Sets the url pattern for each page.
urlpatterns = [
    path('',  HomeView.as_view(), name="home"),
    path('Posts/<int:pk>', PostView.as_view(), name='details'),
    path('Add_Post/', AddPostView.as_view(), name='posts'),
    path('Posts/Edit/<int:pk>', EditPostView.as_view(), name='edit'),
    path('Posts/<int:pk>/deletePost/',
         DeletePostView.as_view(), name='delete'),
    path('Posts/<int:pk>/add_comment/',
         CommentView.as_view(), name='add_comment'),
    path('Add_Category/', AddCategoryView.as_view(),
         name='category'),
    path('Category/<str:category>/', CategoryView, name='category_page'),
    path('Category_list/', CategoryListView, name='category_list'),
    path('Like/<int:pk>', LikePostView, name='like'),
]
