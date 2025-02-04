from django.urls import path
from movie.views import index, movie

urlpatterns = [
    path('', index, name='index'),
    path('<int:movie_id>/', movie, name='movie'),
]
