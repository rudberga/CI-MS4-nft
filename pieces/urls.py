from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_pieces, name='pieces'),
    path('<int:piece_id>/', views.piece_detail, name='piece_detail'),
    path('add/', views.add_piece, name='add_piece'),
]
