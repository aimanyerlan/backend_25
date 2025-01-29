from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie/movie_list.html', {'movies': movies})

def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie-list')
    else:
        form = MovieForm()
    return render(request, 'movie/movie_form.html', {'form': form})

