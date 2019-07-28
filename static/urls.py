from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('<int:bid>/', views.BlogView.as_view(), name='blog'),
    path('<int:pid>/comments', views.PostView.as_view(), name='post'),
    path('<int:bid>/addpost', views.make_post, name='makepost'),
    path('<int:pid>/addcomment', views.addComment, name='addcomment'),
    path('<int:profid>/profile', views.profile, name='user'),
    path('<int:pid>/addLike', views.addLike, name='addLike'),
    path('<int:pid>/addDislike', views.addDislike, name='addDislike'),
    path('signup', views.make_account, name='makeaccount'),
    path('', views.log_in, name='signin')
]
