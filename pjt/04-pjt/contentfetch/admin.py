from django.contrib import admin
from .models import StockData, UserStock

# Register your models here.
admin.site.register(StockData)
admin.site.register(UserStock)
