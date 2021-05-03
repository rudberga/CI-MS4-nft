from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from favourite.models import Favourite
from pieces.models import Piece


def add_to_fav(request):
    piece_name = request.POST.get('piece_name')
    piece_obj = Piece.objects.get(id=piece_name)
    fav_product = Favourite.objects.filter(user=request.user,
                                           piece=piece_obj, status=True).last()
    if fav_product:
        fav_product.status = False
        fav_product.save()
    else:
        fav_product = Favourite.objects.filter(
            user=request.user,
            piece=piece_obj).last()
        if fav_product:
            fav_product.status = True
            fav_product.save()
        else:
            Favourite.objects.create(user=request.user,
                                     piece=piece_obj,
                                     status=True)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
