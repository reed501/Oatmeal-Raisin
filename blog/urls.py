from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.log_in, name='signin'),
    path('signup', views.make_account, name='makeaccount'),
    path('logout', views.log_out, name='logout'),
    path('<int:profid>-<str:user>/edit', views.edit_profile, name='editprofile'),
    path('<int:profid>-<str:user>/<int:bid>-blog', views.BlogView.as_view(), name='blog'),
    path('<int:profid>-<str:user>/<int:bid>-blog/<int:pid>-post', views.PostView.as_view(), name='post'),
    path('<int:profid>-<str:user>', views.ProfileView.as_view(), name='user'),
    path('<int:profid>-<str:user>/addblog', views.addBlog, name='addblog'),
    path('<int:profid>-<str:user>/<int:bid>-blog/addpost', views.addPost, name='addpost'),
    path('<int:profid>-<str:user>/<int:bid>-blog/<int:pid>-post/addcomment', views.addComment, name='addcomment'),
    path('<int:profid>-<str:user>/<int:bid>-blog/<int:pid>-post/addLike', views.addLike, name='addLike'),
    path('<int:profid>-<str:user>/<int:bid>-blog/<int:pid>-post/addDislike', views.addDislike, name='addDislike')
]
