
# Create your models here.
from django.db import models

class Song(models.Model):
    C_Title = models.CharField(max_length=1000)
    C_Artist = models.CharField(max_length=1000)
    C_Album = models.CharField(max_length=1000)
    C_lyrics = models.TextField()

    def __str__(self):
        return self.C_Title + ' - ' + self.C_Artist
