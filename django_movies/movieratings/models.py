from django.db import models

# Create your models here.

# Create your models here.
class Movie(models.Model):
    movie_id = models.IntegerField(default=0)
    title = models.CharField(max_length=160)
    #genres = models.CharField(max_length=160)


class Rater(models.Model):
    user_id = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=2)
    occupation = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)


class Rating(models.Model):
    user_id = models.CharField(max_length=8)
    movie_id = models.IntegerField(default=0)
    rating = models.CharField(max_length=5)
    timestamp = models.CharField(max_length=20)
