import datetime

from django.db import models
from django.utils import timezone

class Profile(models.Model):
    name = models.CharField(max_length=40)
    birth = models.DateField()
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    bio = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Blog(models.Model):
    blog_name = models.CharField(max_length=50)
    blog_desc = models.CharField(max_length=200)
    blog_date = models.DateField()

    def __str__(self):
        return self.blog_name

class ProfileBlog(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=10000)
    hidden = models.BooleanField(default=False)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    date = models.DateField()

    def __str__(self):
        return self.title

class BlogPost(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.CharField(max_length=1000)
    date = models.DateField()

    def __str__(self):
        return self.date

class CommentProfile(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    profile = models.ForeignKey(Post, on_delete=models.CASCADE)

class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
