from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:bid>/', views.posts, name='post'),
    path('<int:bid>/<int:pid>/', views.comments, name='comment')
]
