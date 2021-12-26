from django.db import models

# Create your models here.

class Feedback (models.Model):

    username = models.TextField()
    proposal = models.TextField()
    date     = models.DateTimeField()

    def __str__ (self):
        self.username
        self.date
        return self.proposal
