from django.shortcuts import render, get_object_or_404

from gameplay.models import Game


def game_detail(request, id):
    game = get_object_or_404(Game, pk=id)
    context = {'game': game}
    if game.is_users_move(request.user):
        context['form'] = MoveForm()
    return render(request, 'gameplay/game_detail.html', context)