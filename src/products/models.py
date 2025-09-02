from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.TextField()
    price = models.TextField()
    description = models.TextField()
    summary = models.TextField(default="This is my default summar!")