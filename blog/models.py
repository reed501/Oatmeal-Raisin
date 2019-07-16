import datetime

from django.db import models
from django.utils import timezone

class Profile(models.Model):
    name = models.CharField(max_length=40)
    birth = models.DateField()
    password = models.CharField(max_length=40)
    email = models.CharField(max_length=40)

class Blog(models.Model):
    blog_name = models.CharField(max_length=20)
    blog_desc = models.CharField(max_length=200)

    def __str__(self):
        return self.blog_name

class ProfileBlog(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

class Post(models.Model):
    content = models.CharField(max_length=10000)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    date = models.DateField()

class BlogPost(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.CharField(max_length=1000)
    date = models.DateField()

class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
