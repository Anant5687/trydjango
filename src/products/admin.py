from django.contrib import admin

# Register your models here.

from .models import Products   # import the model class

admin.site.register(Products)   # register the model
