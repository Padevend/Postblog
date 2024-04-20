from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.overview, name='home'),
    path('delete/<int:post_id>/', views.deletePost, name='delete'),
    path('edit/<int:post_id>/', views.editPost, name='edit_post'),
    path('newpost/', views.addPost, name='add_post'),
    path('comments/', views.commentView, name='comments'),
]
