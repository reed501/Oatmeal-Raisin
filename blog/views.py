from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from django.utils.timezone import datetime
from django.db.models import F

from .models import Blog, Post, BlogPost, Comment, PostComment, Profile
from .forms import PostForm, CommentForm
from django.contrib.auth.models import User


class IndexView(generic.ListView):
    model = Blog
    template_name = 'blog/index.html'

class PostView(generic.ListView):
    context_object_name = 'posts'
    template_name = 'blog/blog.html'

    def get_queryset(self):
        return Post.objects.filter(blogpost__blog_id=self.kwargs['bid'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog'] = Blog.objects.get(id=self.kwargs['bid'])
        return context

class CommentView(generic.ListView):
    context_object_name = 'comments'
    template_name = 'blog/comment.html'
    
    def get_queryset(self):
        return Comment.objects.filter(postcomment__post_id=self.kwargs['pid'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.get(id=self.kwargs['pid'])
        return context

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

def addComment(request, pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            cont = form.cleaned_data['content']
            comm = Comment.objects.create(content=cont, date=datetime.now())
            comm.save()
            post = PostComment.objects.create(post_id=pid, comment_id=comm.id)
            post.save()
            #CommentProfile.objects.create(comment_id=comm).update(profile=user)
            return HttpResponseRedirect('/')
    else:
        form = CommentForm()
    return render(request, 'blog/addcomment.html', {'form' : form})

def profile(request,profid):
    person = Profile.objects.get(id=profid)
    args = {'user': person}
    return render(request, 'blog/profile.html', args)

def addLike(request, pid):
    Post.objects.filter(id=pid).update(likes=F('likes')+1)
    return HttpResponseRedirect('/')

def addDislike(request, pid):
    Post.objects.filter(id=pid).update(dislikes=F('dislikes')+1)
    return HttpResponseRedirect('/')

