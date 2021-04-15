from django.shortcuts import render
from .models import Piece


def all_pieces(request):
    """ A view to show all pieces, including sorting and search queries """

    pieces = Piece.objects.all()

    context = {
        'pieces': pieces,
    }

    return render(request, 'pieces/pieces.html', context)
