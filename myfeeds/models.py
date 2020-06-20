from django.db import models


class Track(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Feed(models.Model):
    name = models.CharField(max_length=100)
    tracks = models.ManyToManyField(Track)

    def __str__(self):
        return self.name
