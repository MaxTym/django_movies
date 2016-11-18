from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^movie/([0-9]+)', views.movie_detail, name='movie'),
    url(r'^movie_list$', views.movie_list, name='movie_list')
]
