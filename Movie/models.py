# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class movies(models.Model):
    movie_name = models.CharField(max_length=100)
    actor = models.CharField(max_length=100)
    genre = models.CharField(max_length=10)
    movie_logo = models.FileField()

    def __str__(self):
        return self.movie_name + '-->' + self.actor


class song(models.Model):
    movie = models.ForeignKey(movies, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_name = models.CharField(max_length=50)
    audio = models.FileField(default='')

    def __str__(self):
        return self.song_name

