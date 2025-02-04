from django.shortcuts import render, redirect
from .models import Movie

def index(request):
    if request.method == "GET":
        movies = Movie.objects.all
        context = {'movies': movies}
        return render(request, "movie/index.html", context)
    
def movie(request, movie_id):
    if request.method == "GET":
        m = Movie.objects.get(pk=movie_id)
        context = {'my_movie': m}
        return render(request, "movie/movie.html", context)
    