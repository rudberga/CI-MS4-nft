from django.contrib import admin
from favourite.models import Favourite


class FavouriteAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'piece',
        'status',
    )


admin.site.register(Favourite, FavouriteAdmin)
