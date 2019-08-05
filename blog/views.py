from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.urls import reverse
from django.views import generic
from django.utils.timezone import datetime
from django.db.models import F
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import Blog, Post, BlogPost, Comment, PostComment, Profile, ProfileBlog, CommentProfile
from .forms import PostForm, SignUp, LogIn, CommentForm, BlogForm, EditForm

class BlogView(generic.ListView):
    context_object_name = 'posts'
    template_name = 'blog/blog.html'

    def get_queryset(self):
        return Post.objects.filter(blogpost__blog_id=self.kwargs['bid'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog'] = blog = Blog.objects.get(id=self.kwargs['bid'])
        context['profile'] = prof = Profile.objects.get(id=self.kwargs['profid'])
        context['useraccount'] = User.objects.get(id=prof.user_id)
        return context

class PostView(generic.ListView):
    context_object_name = 'comments'
    template_name = 'blog/post.html'

    def get_queryset(self):
        return Comment.objects.filter(postcomment__post_id=self.kwargs['pid'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.get(id=self.kwargs['pid'])
        context['blog'] = Blog.objects.get(id=self.kwargs['bid'])
        context['profile'] = prof = Profile.objects.get(id=self.kwargs['profid'])
        context['useraccount'] = User.objects.get(id=prof.user_id)
        return context

class ProfileView(generic.ListView):
    context_object_name = 'blogs'
    template_name = 'blog/profile.html'

    def get_queryset(self):
        return Blog.objects.filter(profileblog__profile_id=self.kwargs['profid'])

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = prof = Profile.objects.get(id=self.kwargs['profid'])
        context['useraccount'] = User.objects.get(id=prof.user_id)
        return context

def log_in(request):
    if request.method == 'POST':
        form = LogIn(request.POST)

        if form.is_valid():
            name_form = form.cleaned_data['username']
            password_form = form.cleaned_data['password']

            user = authenticate(request, username=name_form, password=password_form)
            if user is not None:
                login(request, user)
                prof = Profile.objects.get(user_id=user.id)
                return redirect('blog:user', profid=prof.id, user=user.username)
            else:
                return HttpResponseRedirect('/') #FAILED LOGIN, BACK TO LOGIN FORM
    else:
        form = LogIn()

    return render(request, 'blog/login.html', {'form': form})

def make_account(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']

            if password1 == password2:
                user = User.objects.create_user(name, email, password1)
                user.first_name = name
                user.save()
                prof = Profile.objects.create(user_id=user.id, birth=datetime.now(), bio="", pic='default.png')
                login(request, user)
                return redirect('blog:user', profid=prof.id, user=user.username)
            else:
                return HttpResponseRedirect('signup') #password doesnt match
    else:
        form = SignUp()

    return render(request, 'blog/signup.html', {'form': form})

def log_out(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect('/')

def edit_profile(request, profid, user):
    if request.method == 'POST':
        profile = Profile.objects.get(id=profid)
        form = EditForm(request.POST)
        if form.is_valid():
            userx = request.user
            name = User.objects.get(id=userx.id)
            if form.data['fname'] == '':
                fname = name.first_name
            else:
                fname = form.cleaned_data['fname']
            if form.data['lname'] == '':
                lname = name.last_name
            else:
                lname = form.cleaned_data['lname']
            if form.data['bio'] == '':
                bio = profile.bio
            else:
                bio = form.cleaned_data['bio']
            if request.user.is_authenticated:
                Profile.objects.filter(id=profid).update(bio=bio)
                User.objects.filter(id=userx.id).update(first_name=fname, last_name=lname)
            return redirect('blog:user', profid=profid, user=user)
        else:
            print (form.errors)
    else:
        form = EditForm()
    return render(request, 'blog/editprofile.html', {'form': form})

def addBlog(request, profid, user):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            desc = form.cleaned_data['desc']
            blog = Blog.objects.create(blog_name=title, blog_desc=desc, blog_date=datetime.now())
            blog.save()
            pb = ProfileBlog.objects.create(profile_id=profid, blog_id=blog.id)
            pb.save()
            return redirect('blog:blog', profid=profid, user=user, bid=blog.id)
    else:
        form = BlogForm()
    return render(request, 'blog/addblog.html', {'form': form})

def addPost(request, profid, user, bid):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            post = Post.objects.create(title=title, content=content, hidden=False, likes=0, dislikes=0, date=datetime.now())
            post.save()
            bp = BlogPost.objects.create(blog_id=bid, post_id=post.id)
            bp.save()
            return redirect('blog:blog', profid=profid, user=user, bid=bid)

    else:
        form = PostForm()
    return render(request, 'blog/addpost.html', {'form': form})

def addComment(request, profid, user, bid, pid):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            cont = form.cleaned_data['content']
            comm = Comment.objects.create(content=cont, date=datetime.now())
            comm.save()
            post = PostComment.objects.create(post_id=pid, comment_id=comm.id)
            post.save()
            profile = Profile.objects.get(user_id=request.user.id)
            cp = CommentProfile.objects.create(comment_id=comm.id, profile_id=profile.id)
            cp.save()
            return redirect('blog:post', profid=profid, user=user, bid=bid, pid=pid)
    else:
        form = CommentForm()
    return render(request, 'blog/addcomment.html', {'form' : form})

def addLike(request, profid, user, bid, pid):
    Post.objects.filter(id=pid).update(likes=F('likes')+1)
    return redirect('blog:post', profid=profid, user=user, bid=bid, pid=pid)

def addDislike(request, profid, user, bid, pid):
    Post.objects.filter(id=pid).update(dislikes=F('dislikes')+1)
    return redirect('blog:post', profid=profid, user=user, bid=bid, pid=pid)
