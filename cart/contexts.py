from django.shortcuts import get_object_or_404
from pieces.models import Piece


def cart_contents(request):

    cart_items = []
    total = 0
    piece_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        piece = get_object_or_404(Piece, pk=item_id)
        total += quantity * piece.price
        piece_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'piece': piece,
        })

    grand_total = total

    context = {
        'cart_items': cart_items,
        'total': total,
        'piece_count': piece_count,
        'grand_total': grand_total,
    }

    return context
