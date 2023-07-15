from django.db import models
from django.core import validators

class user(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.TextField(blank=True)
    bio = models.TextField()
    degree = models.CharField(max_length=100)
    dp = models.FileField(upload_to="student")
    

# Create your models here.
