from django.db import models

class People(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
