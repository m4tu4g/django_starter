from django.db import models

# Create your models here.
class Fren(models.Model):
    name = models.CharField(max_length=8)