from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    description = models.TextField()
    isbn = models.CharField(max_length=10)
    pubdate = models.DateField()
    price = models.IntegerField()
    adult = models.BooleanField()