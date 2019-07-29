from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.log_in, name='signin'),
    path('signup', views.make_account, name='makeaccount'),
    path('logout', views.log_out, name='logout'),
    path('<int:bid>/blog', views.BlogView.as_view(), name='blog'),
    path('<int:pid>/comments', views.PostView.as_view(), name='post'),
    path('<int:profid>/profile', views.profile, name='user'),
    path('<int:profid>/addblog', views.addBlog, name='addblog'),
    path('<int:bid>/addpost', views.addPost, name='addpost'),
    path('<int:pid>/addcomment', views.addComment, name='addcomment'),
    path('<int:pid>/addLike', views.addLike, name='addLike'),
    path('<int:pid>/addDislike', views.addDislike, name='addDislike')
]
