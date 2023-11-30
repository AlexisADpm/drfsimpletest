from django.db import models

# Create your models here.
class Poryect(models.Model):
    title = models.CharField(max_length=200)
    desctiption = models.TextField()
    technology = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)