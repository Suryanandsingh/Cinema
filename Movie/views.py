# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
#from django.http import HttpResponse  for HttpResponse viewer
# from django.template import loader  for template viewer
# from django.http import Http404
from .models import movies
from django.contrib.auth.models import User
from .forms import UserFrom
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist


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
    movie = get_object_or_404(movies, pk=movie_id)
    context = {
        'movie':movie,
    }
    return render(request, 'Movie/detail.html', context)



def Login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/home/')
            else:
                messages.error(request, 'Username or password did not match')
        except ObjectDoesNotExist:
            print("Invalide user")
    return render(request, 'Movie/login.html')



def registeration(request):
    if request.method == 'POST':
        form = UserFrom(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Your Registration successfully.')
            return redirect('/home/')

    else:
        form = UserFrom()
    return render(request, 'Movie/register.html', {'form':form})