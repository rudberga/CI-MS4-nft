from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_pieces, name='pieces'),
    path('<piece_id>', views.piece_detail, name='piece_detail'),
]
