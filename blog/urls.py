from django.urls import path
from . import views

app_name = 'blog'  # avoid conflict
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),  # as_view() is the 'view()' of class IndexView
    path('post/<pk>', views.ArticleView.as_view(), name='detail'),
    path('archive/<year>/<month>', views.ArchivesView.as_view(), name='archive'),
    path('category/<pk>', views.CategoryView.as_view(), name='category'),
]
