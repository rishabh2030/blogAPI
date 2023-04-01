from django.urls import path,include
from .views import BlogCreate,BlogPostView,blogPostDetailView,DeleteBlogView,EditBlogView,SearchBlog
from rest_framework.routers import DefaultRouter

app_name = 'blog'

urlpatterns = [
    path('create_blog_post/',BlogCreate.as_view(),name='blog_post'),
    path('view_blog_post/',BlogPostView.as_view(),name='blog_post_view'),
    path('Get_notice/<int:pk>/', blogPostDetailView.as_view(), name='blog_post_detail'),
    path('blog_Delete/<int:pk>/',DeleteBlogView.as_view(), name='blog_delete'),
    path('blog_Edit/<int:pk>/',EditBlogView.as_view(), name='blog_Edited'),
    path('blog_Search/',SearchBlog.as_view(), name='Search_Blog'),
]
