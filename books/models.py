from statistics import mode
from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    name = models.CharField(max_length=150)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    author = models.CharField(max_length=100)
