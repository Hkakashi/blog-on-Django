from django.contrib.syndication.views import Feed

from .models import Body


class AllPostsRssFeed(Feed):
    title = "Liu Peng's Blog"
    link = "www.starrymood.fun"
    description = "Liu Peng's Blog"

    def items(self):
        return Body.objects.all()

    def item_title(self, item):
        return '[%s] %s' % (item.category, item.title)

    def item_description(self, item):
        return item.content
