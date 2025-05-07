from django.db import models

# Create your models here.
class APIInfo(models.Model):
    name = models.CharField(max_length=200)
    descripiton = models.TextField()
    api_url = models.URLField()
    documenation_url = models.URLField()
    auth_required = models.BooleanField()
    sample_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

