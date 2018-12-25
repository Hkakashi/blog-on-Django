from django.urls import path
from . import views

app_name = 'blog'  # avoid conflict
urlpatterns = [
    path('', views.index, name='index'),
    path('post/<pk>', views.detail, name='detail'),
    path('archive/<year>/<month>', views.archive, name='archive'),
    path('category/<pk>', views.category, name='category'),
]
