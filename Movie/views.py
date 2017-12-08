# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse  for HttpResponse viewer
# from django.template import loader  for template viewer
# from django.http import Http404
from .models import movies

def index(request):
    all_movie = movies.objects.all()
    context ={
        'all_movie':all_movie,
    }
    return render(request, 'Movie/index.html', context)


def detail(request, movie_id):
    '''try:
        movieID = movies.objects.get(pk=movie_id)
    except movies.DoesNotExist:
        raise Http404('Movie does not exist')'''
    #same as above is
    movieID = get_object_or_404(movies, pk=movie_id)
    context = {
        'movieID':movieID,
    }
    return render(request, 'Movie/detail.html', context)