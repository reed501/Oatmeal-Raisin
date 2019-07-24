from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:bid>/', views.PostView.as_view(), name='post'),
    path('<int:pid>/comments', views.comments, name='comment'),
    path('<int:bid>/addpost', views.make_post, name='makepost'),
    path('signup', views.make_account, name='makeaccount'),
    # path('<int:bid>/signup', views.log_in, name='makeaccount'),
]
