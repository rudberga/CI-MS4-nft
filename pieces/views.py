from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Piece


def all_pieces(request):
    """ A view to show all pieces, including sorting and search queries """

    pieces = Piece.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('pieces'))
           
            queries = Q(name__icontains=query) | Q(type_of_piece__icontains=query)
            pieces = pieces.filter(queries)

    context = {
        'pieces': pieces,
        'search_term': query,
    }

    return render(request, 'pieces/pieces.html', context)


def piece_detail(request, piece_id):
    """ A view to show an individual piece """

    piece = get_object_or_404(Piece, pk=piece_id)

    context = {
        'piece': piece,
    }

    return render(request, 'pieces/piece_detail.html', context)
