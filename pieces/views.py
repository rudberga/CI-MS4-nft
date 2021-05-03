from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from comments.models import Comment
from favourite.models import Favourite
from allauth.account.forms import LoginForm

from .models import Category, Piece
from .forms import ProductForm


def all_pieces(request):
    """ A view to show all pieces, including sorting and search queries """

    pieces = Piece.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                pieces = pieces.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            pieces = pieces.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            pieces = pieces.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               "You forgot to enter any search criteria!")
                return redirect(reverse('pieces'))

            queries = Q(name__icontains=query) | Q(type_of_piece__icontains=query)
            pieces = pieces.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'pieces': pieces,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'login_form': LoginForm(),
    }

    return render(request, 'pieces/pieces.html', context)


def piece_detail(request, piece_id):
    """ A view to show an individual piece """

    piece = get_object_or_404(Piece, pk=piece_id)
    comments = Comment.objects.filter(piece=piece_id)
    fav_product = Favourite.objects.filter(piece=piece_id).last()

    context = {
        'piece': piece,
        'comments': comments,
        'fav_product': fav_product,
        'login_form': LoginForm(),
    }

    return render(request, 'pieces/piece_detail.html', context)


@login_required
def add_piece(request):
    """ Add a piece to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added piece!')
            return redirect(reverse('add_piece'))
        else:
            messages.error(request, 'Failed to add piece. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'pieces/add_piece.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_piece(request, piece_id):
    """ Edit a piece in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    piece = get_object_or_404(Piece, pk=piece_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=piece)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated piece!')
            return redirect(reverse('piece_detail', args=[piece.id]))
        else:
            messages.error(request, 'Failed to update piece. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=piece)
        messages.info(request, f'You are editing {piece.name}')

    template = 'pieces/edit_piece.html'
    context = {
        'form': form,
        'piece': piece,
    }

    return render(request, template, context)


@login_required
def delete_piece(request, piece_id):
    """ Delete a piece from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    piece = get_object_or_404(Piece, pk=piece_id)
    piece.delete()
    messages.success(request, 'Piece deleted!')
    return redirect(reverse('pieces'))
