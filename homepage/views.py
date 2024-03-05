from django.shortcuts import render
from game.models import Game

def home(request):
    games = Game.objects.all()
    return render(request, 'homepage/homepage.html', {'games': games})

def genre(request):
    unique_genres = Game.objects.values_list('genre', flat=True).distinct()
    context = {
        'unique_genres': unique_genres,
    }
    return render(request, 'homepage/genre.html', context)

