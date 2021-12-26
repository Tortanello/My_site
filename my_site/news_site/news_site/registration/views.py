from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
from .forms import UserForm_ERROR_NAME

from django.contrib import auth
from django.contrib.auth import login, authenticate

from registration.models import Register_db as model_re

from django.contrib.auth.models import User

from django.db import IntegrityError

from django.shortcuts import redirect

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import logout

def auntification (request):
    userform = UserForm()
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        # Проверка есть ли такие данные в базе данных
        # Добавления в бд новых данных
        user = authenticate(username = username, email = email, password = password)
        if user is not None:
            login(request, user)
            return redirect ('http://127.0.0.1:8000')
        else: 
            return render (request, 'registration/auntification_block_ERROR.html', {'form': userform})
    else:
        return render (request, 'registration/registration_block.html', {'form': userform})

def registration (request):
    userform = UserForm()
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = User.objects.create_user(username = username, email = email, password = password)
            login(request, user)
        except IntegrityError :
            userform = UserForm_ERROR_NAME()
            return render (request, 'registration/auntification_two_block.html', {'form': userform})
    return render (request, 'registration/auntification_block.html', {'form': userform})

def de_auntification (request):
    if request.user.is_authenticated:
        username = request.user.username
        logout(request)
        return render (request, 'registration/de_auntification.html', {'username': username})
    else :
        return render (request, 'registration/not_de_auntification.html')

def pre_de_auntification (request):
    if request.user.is_authenticated:
        username = request.user.username
        return render (request, 'registration/pre_de_auntification.html', {'username': username})
    else :
        return render (request, 'registration/not_de_auntification.html')
