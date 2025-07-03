from django.urls import path
from .views import movie_list_create, movie_detail, home

urlpatterns = [
    path('', home),
    path('movies/', movie_list_create),
    path('movies/<int:pk>/', movie_detail),
]
