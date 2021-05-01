from django.contrib import admin
from comments.models import Comment


class CommentsAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'piece',
        'pub_date',
        'piece_comment',
    )


admin.site.register(Comment, CommentsAdmin)
