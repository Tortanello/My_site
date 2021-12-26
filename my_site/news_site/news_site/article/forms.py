from django import forms
from article.models import Comment_db
from django.contrib import auth
from django.forms import ModelForm, Textarea
 
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment_db
        fields = ('comment',)
        widgets = {
            'comment': forms.Textarea(attrs={'type': 'text','class': 'form-control', 'id': 'form_comment'}),
        }
