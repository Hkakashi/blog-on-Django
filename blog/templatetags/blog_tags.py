from ..models import Body, Category
from django import template

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
    return Category.objects.all()  # show categories
