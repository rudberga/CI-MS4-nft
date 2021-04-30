from django.contrib.auth.models import User
from django.db import models
from pieces.models import Piece


class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    piece = models.ForeignKey(Piece, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
