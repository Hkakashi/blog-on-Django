from ..models import Body, Category, Tag
from django import template
from django.db.models.aggregates import Count

# define template tags
register = template.Library()


@register.simple_tag()
def get_recent_post(num=5):
    return Body.objects.all().order_by('-created_time')[:num]


@register.simple_tag()
def archive():
    # return a list of dates
    return Body.objects.dates('created_time', 'month', order='DESC')  # archive articles by month in descending order


@register.simple_tag()
def get_categories():
    return Category.objects.annotate(num_posts=Count('body')).filter(num_posts__gt=0)

@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_posts=Count('body')).filter(num_posts__gt=0)