from django.shortcuts import render
from movieratings import models
from .models import Movie, Rater, Rating
from django.http import HttpResponse
from django.db.models import Count, Avg
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.views.generic import View, RedirectView, ListView
from django.shortcuts import render, redirect, render_to_response, get_object_or_404


def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Welcome to a movie ratings site")


def movie_detail(request, var):
    movie = models.Movie.objects.get(pk=var)
    return render(request, 'movie_detail.html', {'movie':movie})


def movie_list(request):
    movies = models.Movie.objects.all()
    return render(request, 'movie_list.html', {'movies':movies})


def rater_detail(request, var):
    rater = models.Rater.objects.get(pk=var)
    all_ratings = rater.rating_set.order_by("rating")
    return render(request, 'rater_detail.html', {'rater':rater, 'all_ratings': all_ratings})


def rater_list(request):
    raters = models.Rater.objects.all()
    return render(request, 'rater_list.html', {'raters':raters})

def top_20(request):
    top_movies = models.Movie.objects.annotate(avg_rating=Avg('rating__rating')).order_by('-avg_rating')[:20]
    return render(request, 'top_movies.html', {'top_movies':top_movies})


#@login_required(login_url='/accounts/login/')
def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
    else:
        # Return an 'invalid login' error message.
        ...
