from django import forms
from .models import Feedback
from django.contrib import auth
from django.forms import ModelForm, Textarea
 
class Feedback_form(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('proposal',)
        widgets = {
            'proposal': forms.Textarea(attrs={'type': 'text','class': 'form-control', 'id': 'form_comment'}),
        }
