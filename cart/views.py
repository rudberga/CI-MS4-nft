from django.shortcuts import render


def view_cart(request):
    """ View to render the cart page """

    return render(request, 'cart/cart.html')
