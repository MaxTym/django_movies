from django.db import models
from django.urls import reverse
from django.db.models import Avg, Count

class Movie(models.Model):
    title = models.CharField(max_length=160)


    @property
    def get_url(self):
        return reverse('movie_detail', args=[self.pk])


class Rater(models.Model):
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=2)
    occupation = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)


    @property
    def get_url(self):
        return reverse('rater_detail', args=[self.pk])


class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    rating = models.CharField(max_length=5)
    timestamp = models.CharField(max_length=32)


    @property
    def avg_rating(self):
        avg_rating = self.movie.aggregate(avg_movie_rating=Avg('rating'))
        return avg_rating['avg_movie_rating']
