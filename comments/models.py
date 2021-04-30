from django.contrib.auth.models import User
from django.db import models
from pieces.models import Piece


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    piece = models.ForeignKey(Piece, on_delete=models.CASCADE)
    piece_comment = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
