from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):  # as the form is related to a model. otherwise we can use forms.Form
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']
