from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from .models import Blog, Post, BlogPost, Comment, PostComment


class IndexView(generic.ListView):
    model = Blog
    template_name = 'blog/index.html'

def posts(request, bid):
    posts = Post.objects.filter(blogpost__blog_id=bid)
    return render(request, 'blog/blog.html', {'posts': posts})

def comments(request, bid, pid):
    comms = Comment.objects.filter(postcomment__post_id=pid)
    return render(request, 'blog/comment.html', {'comments': comms})
