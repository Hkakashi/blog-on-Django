from django.shortcuts import render_to_response, redirect, get_object_or_404
from blog.models import Body
from .models import Comment
from .forms import CommentForm


# Create your views here.

def post_comment(request, post_pk):
    post = get_object_or_404(Body, pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)  # generate comment object but not commit it to the database
            comment.article = post
            comment.save()
            return redirect(post)  # redirect via model
        else:
            comment_list = Comment.objects.filter(article=post)  # or = article.comment_set.all()  <- .xxx_set.all()
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list}
            return render_to_response('blog/detail.html', context=context)
    return redirect(post)
