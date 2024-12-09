from django.shortcuts import render


def snake_game(request):
    return render(request, 'snake/snake_game.html')
