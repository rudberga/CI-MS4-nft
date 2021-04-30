from django.http import HttpResponseRedirect
from django.shortcuts import redirect

from comments.models import Comment
from pieces.models import Piece


def add_comments(request):
    comment = request.POST.get('comment')
    piece_name = request.POST.get('piece_name')
    piece_obj = Piece.objects.get(id=piece_name)
    Comment.objects.create(user=request.user, piece=piece_obj, piece_comment=comment)
    return redirect('/')
