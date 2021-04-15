from django.contrib import admin
from .models import Piece, Category


class PieceAdmin(admin.ModelAdmin):
    list_display = (
        'id_number',
        'name',
        'artist',
        'category',
        'price',
        'eth_price',
        'year',
        'media',
    )

    ordering = ('id_number',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Piece)
admin.site.register(Category)
