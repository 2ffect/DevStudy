from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    is_published = models.BooleanField()
    creat_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)