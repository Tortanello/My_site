from django.contrib import admin

from article.models import Article_db, Comment_db
# Register your models here.

admin.site.register(Article_db)
admin.site.register(Comment_db)