from django.shortcuts import render, get_object_or_404
from .models import Piece


def all_pieces(request):
    """ A view to show all pieces, including sorting and search queries """

    pieces = Piece.objects.all()

    context = {
        'pieces': pieces,
    }

    return render(request, 'pieces/pieces.html', context)


def piece_detail(request, piece_id):
    """ A view to show an individual piece """

    piece = get_object_or_404(Piece, pk=piece_id)

    context = {
        'piece': piece,
    }

    return render(request, 'pieces/piece_detail.html', context)
