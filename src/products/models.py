from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=150)
    price = models.DecimalField(decimal_places=2, max_digits=1000000)
    description = models.TextField(blank=True, null=True)
    summary = models.TextField(default="This is my default summar!")