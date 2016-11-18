from django.shortcuts import render
from movieratings import models
# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def movie_detail(request, var):
    movie = models.Movie.objects.get(pk=var)
    return render(request, 'movie_detail.html', {'movie':movie})


def movie_list(request):
    movies = models.Movie.objects.all()
    return render(request, 'movie_list.html', {'movies':movies})
