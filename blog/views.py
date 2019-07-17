from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from .models import Blog, Post, BlogPost, Comment, PostComment


class IndexView(generic.ListView):
    model = Blog
    template_name = 'blog/index.html'

#def posts(request, bid):
 #   posts = Post.objects.filter(blogpost__blog_id=bid)
  #  return render(request, 'blog/blog.html', {'posts': posts})

class PostView(generic.ListView):
    context_object_name = 'posts'
    template_name = 'blog/blog.html'
    
    def get_queryset(self):
        return Post.objects.filter(blogpost__blog_id=self.kwargs['bid'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog'] = Blog.objects.get(id=self.kwargs['bid'])
        return context

def comments(request, pid):
    comms = Comment.objects.filter(postcomment__post_id=pid)
    return render(request, 'blog/comment.html', {'comments': comms})
