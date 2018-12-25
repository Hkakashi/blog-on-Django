from django.contrib import admin
from .models import Category, Tag, Body


# Register your models here.

# Show more information at admin page
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Body, PostAdmin)  # register PostAdmin here
