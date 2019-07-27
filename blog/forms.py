from django import forms

class PostForm(forms.Form):
    title = forms.CharField(label='Post title', max_length=50)
    content = forms.CharField(label='Post content', max_length=10000)

class SignUp(forms.Form):
    email = forms.CharField(label='Email', max_length=40, widget=forms.TextInput(attrs={'placeholder': 'Enter Email'}))
    name = forms.CharField(label='Username',max_length=40, widget=forms.TextInput(attrs={'placeholder': 'Enter Username'}))
    password1 = forms.CharField(label='Password',max_length=30, widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    password2 = forms.CharField(label='Re-Enter Password',max_length=30, widget=forms.PasswordInput(attrs={'placeholder': 'Re-Enter Password'}))

class LogIn(forms.Form):
    email = forms.CharField(label='Email', max_length=40, widget=forms.TextInput(attrs={'placeholder': 'Enter Email'}))
    password = forms.CharField(label='Password',max_length=30, widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))

class CommentForm(forms.Form):
    content = forms.CharField(label='Comment', max_length=1000)
