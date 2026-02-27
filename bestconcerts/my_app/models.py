from django.db import models

# Create your models here.

from django.db import models

class Concert(models.Model):
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()

    def __str__(self):
        return self.name
