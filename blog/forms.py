from django import forms

class PostForm(forms.Form):
    title = forms.CharField(label='Post title', max_length=50)
    content = forms.CharField(label='', max_length=10000, widget=forms.Textarea(attrs={'placeholder': 'Post Content', 'cols': "100", 'rows': '20'}))

class SignUp(forms.Form):
    email = forms.CharField(label='Email', max_length=40, widget=forms.TextInput(attrs={'placeholder': 'Enter Email'}))
    name = forms.CharField(label='Username',max_length=40, widget=forms.TextInput(attrs={'placeholder': 'Enter Username'}))
    password1 = forms.CharField(label='Password',max_length=30, widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))
    password2 = forms.CharField(label='Re-Enter Password',max_length=30, widget=forms.PasswordInput(attrs={'placeholder': 'Re-Enter Password'}))

class LogIn(forms.Form):
    username = forms.CharField(label='username', max_length=40, widget=forms.TextInput(attrs={'placeholder': 'Enter Username'}))
    password = forms.CharField(label='Password',max_length=30, widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password'}))

class CommentForm(forms.Form):
    content = forms.CharField(label='', max_length=1000, widget=forms.Textarea(attrs={'placeholder': 'Comment', 'cols': '100', 'rows': '20'}))

class BlogForm(forms.Form):
    title = forms.CharField(label='title', max_length=50)
    desc = forms.CharField(label='', max_length=200, widget=forms.Textarea(attrs={'placeholder': 'Description', 'cols': '100', 'rows': '10'}))

class EditForm(forms.Form):
    fname = forms.CharField(required=False, label='First Name', max_length=20, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    lname = forms.CharField(required=False, label='Last Name', max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    bio = forms.CharField(required=False, label='', max_length=300, widget=forms.Textarea(attrs={'placeholder': 'bio', 'cols': '100', 'rows': '10'}))
