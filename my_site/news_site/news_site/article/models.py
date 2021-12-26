from django.db import models

# Create your models here.

class Comment_db(models.Model):
    username =  models.TextField()
    comment  =  models.CharField(max_length = 500)
    date     =  models.DateTimeField()
    idPost  =   models.IntegerField()

class Article_db(models.Model):
    title  =  models.TextField()
    post   =  models.TextField()
    img    =  models.ImageField()
    date   =  models.DateTimeField()
    # id = models.AutoField() -- вроде автоматически добавляется

    def __str__(self):
        self.post
        self.img
        self.date
        return self.title