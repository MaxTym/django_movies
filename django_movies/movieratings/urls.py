from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^movie/([0-9]+)', views.movie_detail, name='movie'),
    url(r'^movie_list$', views.movie_list, name='movie_list'),
    url(r'^rater/([0-9]+)', views.rater_detail, name='rater'),
    url(r'^rater_list$', views.rater_list, name='rater_list'),
    url(r'^top_movies$', views.top_20, name='top_movies'),
    url(r'^add_rating$', views.add_rating, name="add_rating"),
    url(r'^accounts/logout/$', logout),
    url(r'^accounts/profile/$', views.profile, name='user_profile'),
    url(r'^registration.html/$', views.register_user, name='register_user')
]
