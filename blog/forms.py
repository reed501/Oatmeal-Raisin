from django import forms

class PostForm(forms.Form):
    title = forms.CharField(label='Post title', max_length=50)
    content = forms.CharField(label='Post content', max_length=10000)
