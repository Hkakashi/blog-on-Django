from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Body, Category
import markdown
from comments.forms import CommentForm


# Create your views here.

def index(request):
    article_list = Body.objects.all()
    return render_to_response('blog/index.html', context={'article_list': article_list})


def detail(request, pk):
    article = get_object_or_404(Body, pk=pk)
    article.increase_views()
    article.content = markdown.markdown(article.content,
                                        extensions=[
                                            'markdown.extensions.extra',
                                            'markdown.extensions.codehilite',
                                        ])
    form = CommentForm()
    comment_list = article.comment_set.all()
    context = {'article': article,
               'form': form,
               'comment_list': comment_list
               }
    return render_to_response('blog/detail.html', context=context)


def archive(request, year, month):
    article_list = Body.objects.filter(created_time__year=year, created_time__month=month)
    return render_to_response('blog/index.html', context={'article_list': article_list})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    article_list = Body.objects.filter(category=cate)
    return render_to_response('blog/index.html', context={'article_list': article_list})
