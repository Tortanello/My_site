from django import forms
from registration.models import Register_db
from django.contrib import auth




from django.forms import ModelForm, Textarea
 
class UserForm(forms.ModelForm):
    #username = forms.CharField()
    class Meta:
        # Проблема в том что я думал что эта модель будет использована, но оказалось, что у джанго есть своя бд для users 
        model = Register_db
        fields = ('username', 'email','password')
        # username = forms.CharField()
        # email = forms.EmailField()
        # password = forms.CharField(widget=forms.PasswordInput())

        widgets = {
            'username': forms.TextInput(attrs={'type': 'text','class': 'form-control', 'id': 'form', 'pattern':'^[a-zA-Z]+$'}),
            'email': forms.TextInput(attrs={'type': 'email', 'class': 'form-control', 'id': 'form'}),
            'password': forms.TextInput(attrs={'type': 'password', 'class': 'form-control', 'id': 'form'}),
        }

class UserForm_ERROR_NAME(forms.ModelForm):
    class Meta:
        model = Register_db
        fields = ('username', 'email','password')
        widgets = {
            'username': forms.TextInput(attrs={'type': 'text','class': 'form-control', 'id': 'form', 'placeholder': 'Такой username уже введён', 'pattern':'^[a-zA-Z]+$'}),
            'email': forms.TextInput(attrs={'type': 'email', 'class': 'form-control', 'id': 'form'}),
            'password': forms.TextInput(attrs={'type': 'password', 'class': 'form-control', 'id': 'form'}),
        }