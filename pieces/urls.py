from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_pieces, name='pieces'),
    path('<int:piece_id>/', views.piece_detail, name='piece_detail'),
    path('add/', views.add_piece, name='add_piece'),
    path('edit/<int:piece_id>/', views.edit_piece, name='edit_piece'),
    path('delete/<int:piece_id>/', views.delete_piece, name='delete_piece'),
]
