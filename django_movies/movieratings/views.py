from django.shortcuts import render
from movieratings import models
# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome to a movie ratings site")


def movie_detail(request, var):
    movie = models.Movie.objects.get(pk=var)
    return render(request, 'movie_detail.html', {'movie':movie})


def movie_list(request):
    movies = models.Movie.objects.all()
    return render(request, 'movie_list.html', {'movies':movies})


def rater_detail(request, var):
    rater = models.Rater.objects.get(pk=var)
    return render(request, 'rater_detail.html', {'rater':rater})


def rater_list(request):
    raters = models.Rater.objects.all()
    return render(request, 'rater_list.html', {'raters':raters})
