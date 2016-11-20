from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^movie/([0-9]+)', views.movie_detail, name='movie'),
    url(r'^movie_list$', views.movie_list, name='movie_list'),
    url(r'^rater/([0-9]+)', views.rater_detail, name='rater'),
    url(r'^rater_list$', views.rater_list, name='rater_list'),
    url(r'^top_movies$', views.top_20, name='top_movies'),
     url(r'^login.html$', views.my_view, name="my_view"),
     url(r'^logout.html$', views.logout_view, name="logout_view"),
     url(r'^registration.html/$', views.register_user, name='register_user'),
     url(r'^accounts/profile/$', views.profile_view, name='user_profile')
]
