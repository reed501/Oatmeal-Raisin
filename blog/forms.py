from django import forms

class PostForm(forms.Form):
    title = forms.CharField(label='Post title', max_length=50)
    content = forms.CharField(label='Post content', max_length=10000)

class CommentForm(forms.Form):
    content = forms.CharField(label='Comment', max_length=1000)


