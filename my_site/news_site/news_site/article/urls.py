#from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import ListView, DetailView
from article.models import Article_db
from article.models import Comment_db

# Нужно вынести post в другое приложение потому что на этом файл views заблокирован и легче будет сдлелать новое приложение чем разбираться в этом


urlpatterns = [
    # host_page
    path('', ListView.as_view(queryset = Article_db.objects.all().order_by('-date'),paginate_by = 10,
    template_name = 'article/html_news_articlue.html')),

    path('old_in_top/', ListView.as_view(queryset = Article_db.objects.all().order_by('date'),paginate_by = 10,
    template_name = 'article/html_news_articlue_old_in_top.html')),

    # posts
    path('<int:pk>/',views.PatientDetailView.as_view() ,name='article/post.html'),

    path('old_in_top/<int:pk>/',views.PatientDetailView.as_view() ,name='article/post.html'),

    ]
# <int:pk>/ -- число
# DetailView -- для вывода 1 статьи
# template_name -- шаблон для вывода