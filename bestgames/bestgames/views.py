from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from games.models import Game  

@login_required
def index(request):
    games = Game.objects.select_related('games').all()

    return render(request, 'index.html', {
        'games': games,
    })