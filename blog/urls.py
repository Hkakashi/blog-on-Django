from django.urls import path
from . import views
from .feed import AllPostsRssFeed

app_name = 'blog'  # avoid conflict
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),  # as_view() is the 'view()' of class IndexView
    path('post/<pk>', views.ArticleView.as_view(), name='detail'),
    path('archive/<year>/<month>', views.ArchivesView.as_view(), name='archive'),
    path('category/<pk>', views.CategoryView.as_view(), name='category'),
    path('tag/<pk>', views.TagView.as_view(), name='tag'),
    path('rss', AllPostsRssFeed(), name='rss'),
]
