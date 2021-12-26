from django.urls import path
from . import views

# Распаковать если понадобиться база данных
#from django.views.generic import ListView, DetailView
#from article.models import база данных


urlpatterns = [
    path('', views.registration, name='registration_block'),
    path('auntification/', views.auntification, name='auntification_block'),
    path('de_auntification/', views.de_auntification, name='de_auntification'),
    path('pre_de_auntification/', views.pre_de_auntification, name='pre_de_auntification'),
    #path('', ListView.as_view(queryset = Register_db.objects.all(),
    #template_name = 'article/html_news_articlue.html')),
    ]