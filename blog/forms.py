from django import forms

class PostForm(forms.Form):
    title = forms.CharField(label='Post title', max_length=50)
    content = forms.CharField(label='Post content', max_length=10000)

class SignUp(forms.Form):
    email = forms.CharField(label='Email', max_length=40)
    name = forms.CharField(label='Username',max_length=40)
    password = forms.CharField(label='Password',max_length=30)

class LogIn(forms.Form):
    email = forms.CharField(label='Email', max_length=40)
    password = forms.CharField(label='Password',max_length=30)

class CommentForm(forms.Form):
    content = forms.CharField(label='Comment', max_length=1000)
