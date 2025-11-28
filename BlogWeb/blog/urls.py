from django.urls import path
from . views import *










urlpatterns=[
    path('',Home,name='home'),
    path('create/',CreatePost.as_view(),name='post'),
    path('posts/',listPost.as_view(),name='list-post'),
    path('post/<int:pk>/detail',postDetail.as_view(),name='post-detail'),
    path('post/<int:pk>/update',updatePost.as_view(),name='update-post'),
    path('post/<int:pk>/delete',deletePost.as_view(),name='delete_post'),

]