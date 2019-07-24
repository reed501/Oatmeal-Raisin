from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:bid>/', views.PostView.as_view(), name='post'),
    path('<int:pid>/comments', views.CommentView.as_view(), name='comment'),
    path('<int:bid>/addpost', views.make_post, name='makepost'),
    path('<int:pid>/addcomment', views.addComment, name='addcomment'),
    path('<int:profid>/profile', views.profile, name='user'),

]
