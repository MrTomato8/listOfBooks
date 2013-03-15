from django.db import models

# Create your models here
class Books(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    description = models.CharField(max_length=100, verbose_name="Description")
    author = models.CharField(max_length=100, verbose_name="Author")