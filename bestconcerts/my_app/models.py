from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Concert(models.Model):
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.artist
    
    def get_absolute_url(self):
        return reverse('concert-detail', kwargs={'concert_id': self.id})

class Played_songs(models.Model):
    name = models.TextField(max_length=100)

    def __str__(self):
        return self.name
