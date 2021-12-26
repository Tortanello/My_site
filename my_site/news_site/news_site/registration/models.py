from django.db import models

# Create your models here.

class Register_db(models.Model):

    username = models.TextField()
    email = models.EmailField()
    password = models.TextField()

    def __str__(self):
        self.username
        self.email
        return self.password


