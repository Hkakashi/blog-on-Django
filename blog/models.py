from django.db import models
from django.contrib.auth.models import User  # built-in User model
from django.urls import reverse


# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Body(models.Model):
    title = models.CharField(max_length=70)
    abstract = models.TextField(blank=True)  # An article can have no abstract
    content = models.TextField()  # this is the main content
    tag = models.ManyToManyField(Tag, blank=True)  # An article can have no tag  # one article may have multiple tags
    # on_delete sets how the related models reacts when deleting
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # one category may contains many articles
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # imported from django.contrib.auth.models
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})  # 'blog:detail' correspond to 'APPNAME:URLPATHNAME'

    #  kwargs={'<>': self.xx}   i.e. 'pk'=123 return blog/post/123

    class Meta:
        ordering = ['-created_time', 'title']  # ordered by created time first. if same, sort it by title
