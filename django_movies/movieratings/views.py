from django.shortcuts import render
from movieratings import models

from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Count, Avg
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import View, RedirectView, ListView
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from .forms import RaterForm, RatingForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse



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
        pass


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('movies:index')


def register_user(request):
    if request.method == 'POST':
        rf = RaterForm(request.POST, prefix='rater')
        uf = UserCreationForm(request.POST, prefix='user')
        if rf.is_valid() * uf.is_valid():
            user = uf.save(commit=False)
            user.save()
            rater = rf.save(commit=False)
            rater.user_id = user.id
            rater.id = user.id
            rater.save()
            user = authenticate(username=uf.cleaned_data['username'],
                                password=uf.cleaned_data['password'],
                                )
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
    else:
        rf = RaterForm(prefix='rater')
        uf = UserCreationForm(prefix='user')
    context = {'raterform': rf, 'userform': uf}
    return render(request, 'registration/registration.html', context)
