from django.shortcuts import render, get_object_or_404

from gameplay.models import Game


def game_detail(request, id):
    game = get_object_or_404(Game, pk=id)
    return render(request, 'gameplay/game_detail.html', {'game': game})
