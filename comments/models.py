from django.db import models


# Create your models here.

class Comment(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    comment_time = models.TimeField(auto_now_add=True)  # set comment time as now

    article = models.ForeignKey('blog.Body', on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:20]
