# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import movies, song

admin.site.register(movies)
admin.site.register(song)
