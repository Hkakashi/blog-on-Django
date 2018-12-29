from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Body, Category
import markdown
from comments.forms import CommentForm
from django.views.generic import ListView, DetailView


# Create your views here.


# def index(request):
#     article_list = Body.objects.all()
#     return render_to_response('blog/index.html', context={'article_list': article_list})

class IndexView(ListView):
    model = Body
    template_name = 'blog/index.html'
    context_object_name = 'article_list'


# def detail(request, pk):
#     article = get_object_or_404(Body, pk=pk)
#     article.increase_views()
#     article.content = markdown.markdown(article.content,
#                                         extensions=[
#                                             'markdown.extensions.extra',
#                                             'markdown.extensions.codehilite',
#                                         ])
#     form = CommentForm()
#     comment_list = article.comment_set.all()
#     context = {'article': article,
#                'form': form,
#                'comment_list': comment_list
#                }
#     return render_to_response('blog/detail.html', context=context)


class ArticleView(DetailView):
    model = Body
    template_name = 'blog/detail.html'
    context_object_name = 'article'

    def get(self, request, *args, **kwargs):
        response = super(ArticleView, self).get(request, *args, **kwargs)
        # must call get() first so that it knows which object is being showed
        self.object.increase_views()  # add number of views
        return response  # return a HttpResponse object

    def get_object(self, queryset=None):
        # render markdown content
        post = super(ArticleView, self).get_object(queryset=None)
        post.content = markdown.markdown(post.content,
                                         extensions=[
                                             'markdown.extensions.extra',
                                             'markdown.extensions.codehilite',
                                             'markdown.extensions.toc',
                                         ])
        return post

    def get_context_data(self, **kwargs):
        # render comment list and form
        context = super(ArticleView, self).get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context.update({
            'form': form,
            'comment_list': comment_list
        })
        return context


# def archive(request, year, month):
#     article_list = Body.objects.filter(created_time__year=year, created_time__month=month)
#     return render_to_response('blog/index.html', context={'article_list': article_list})


class ArchivesView(IndexView):
    def get_queryset(self):
        year = self.kwargs.get('year')  # get the parameters
        month = self.kwargs.get('month')
        return super(ArchivesView, self).get_queryset().filter(created_time__year=year,
                                                               created_time__month=month
                                                               )


# def category(request, pk):
#     cate = get_object_or_404(Category, pk=pk)
#     article_list = Body.objects.filter(category=cate)
#     return render_to_response('blog/index.html', context={'article_list': article_list})


class CategoryView(IndexView):
    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)
