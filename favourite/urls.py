from django.urls import path
from . import views

urlpatterns = [
    path('add_fav', views.add_to_fav, name='add_fav'),
]