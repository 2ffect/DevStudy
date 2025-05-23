from django.db import models
from django.conf import settings

# Create your models here.

class Store(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    is_franchise = models.BooleanField(default=False)

    def __str__(self):
        return self.address
    

class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    price = models.IntegerField()
    adult = models.BooleanField(default=False)

    def __str__(self):
        return self.name