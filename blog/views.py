from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils.timezone import datetime

from .models import Blog, Post, BlogPost, Comment, PostComment, Profile, ProfileBlog
from .forms import PostForm, SignUp, LogIn


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

def make_account(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']

            profile = Profile.objects.create(email=email, name=name, password=password, birth=datetime.now(), bio="")
            profile.save()
            
            return HttpResponseRedirect('/')

    else:
        form = SignUp()

    return render(request, 'blog/signup.html', {'form': form})

def make_post(request, bid):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            post = Post.objects.create(title=title, content=content, hidden=False, likes=0, dislikes=0, date=datetime.now())
            post.save()
            bp = BlogPost.objects.create(blog_id=bid, post_id=post.id)
            bp.save()
            return HttpResponseRedirect('/')

    else:
        form = PostForm()

    return render(request, 'blog/addpost.html', {'form': form})
