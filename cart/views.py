from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages
from allauth.account.forms import LoginForm

from pieces.models import Piece


def view_cart(request):
    """ Context for login modal """
    context = {
        'login_form': LoginForm(),
    }
    """ View to render the cart page """

    return render(request, 'cart/cart.html', context)


def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    piece = get_object_or_404(Piece, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request,
                             (f'Updated {piece.name} '
                              f'quantity to {cart[item_id]}'))
    else:
        cart[item_id] = quantity
        messages.success(request,
                             (f'Added {piece.name} '
                              f'to {cart[item_id]}'))

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """Adjust the quantity of the piece in cart"""

    piece = get_object_or_404(Piece, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request,
                         (f'Updated {piece.name} '
                          f'quantity to {cart[item_id]}'))
    else:
        cart.pop(item_id)
        messages.success(request,
                         (f'Removed {piece.name} '
                          f'from your bag'))

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Remove the item from the shopping bag"""
    piece = get_object_or_404(Piece, pk=item_id)
    try:
        cart = request.session.get('cart', {})

        cart.pop(item_id)
        messages.success(request, f'Removed {piece.name} from cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
