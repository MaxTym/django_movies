from __future__ import unicode_literals
import csv
from django.db import migrations
import time


def add_movie(apps, schema_editor):
    Movie = apps.get_model("movieratings", "Movie")
    with open('/users/hrumba/week4/day2/django_movies/u.item', encoding="latin-1") as f:
        reader = csv.reader(f, delimiter='|')
        for i in reader:
            movie = Movie(title=i[1])
            movie.save()


def add_rating(apps, schema_editor):
    Rating = apps.get_model("movieratings", "Rating")
    with open('/users/hrumba/week4/day2/django_movies/u.data', encoding="latin-1") as f:
        reader = csv.reader(f, delimiter='\t')
        for i in reader:
            rating = Rating(rater_id=i[0], movie_id=i[1], rating=i[2], timestamp=time.ctime(int(i[3])))
            rating.save()


def add_rater(apps, schema_editor):
    with open("/users/hrumba/week4/day2/django_movies/u.user") as f:
        r = csv.reader(f, delimiter='|')
        Rater = apps.get_model("movieratings", "Rater")
        for i in r:
            m = Rater(age=i[1], gender=i[2], occupation=i[3], zip_code=i[4])
            m.save()


class Migration(migrations.Migration):

    dependencies = [
        ('movieratings', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_movie),
        migrations.RunPython(add_rating),
        migrations.RunPython(add_rater)
    ]
