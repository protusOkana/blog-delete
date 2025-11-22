from django.shortcuts import render
from django.views.generic import CreateView,DetailView,DeleteView,UpdateView,ListView
from django.urls import reverse_lazy
from . models import *
from django.views.generic import UpdateView,DeleteView,DeleteView
from blog.models import *

# Create your views here.
class CreatePost(CreateView):
    model=blogPost
    fields=['title','content']
    template_name='blog/create-post.html'
    success_url=reverse_lazy('home')

def Home(request):
    return render(request,'blog/index.html')
class listPost(ListView):
    model=blogPost
    context_object_name='posts'
    template_name='blog/list-posts.html'
class postDetail(DetailView):
    model=blogPost
    template_name='blog/post_detail.html'
    context_object_name='pt'
class updatePost(UpdateView):
    model=blogPost
    fields=['title','content']
    template_name='blog/create-post.html'
    success_url=reverse_lazy('list-post')
class deletePost(DeleteView):
    model=blogPost
    context_object_name='del'
    template_name='blog/delete_post.html'
    success_url=reverse_lazy('list-post')