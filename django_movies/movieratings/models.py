from django.db import models
from django.urls import reverse


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


class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    rating = models.CharField(max_length=5)
    timestamp = models.CharField(max_length=32)
