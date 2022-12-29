from django.urls import path
from . import views

urlpatterns = [
    path('films/', views.films_view, name='films'),
    path('film_update/<int:pk>/', views.film_update, name='film_update'),
    path('film_create/', views.film_create, name='film_create'),

    path('cinemas/', views.cinemas, name='cinemas'),
    path('cinema_create/', views.cinema_create, name='cinema_create'),
    path('cinemas/delete/<int:pk>/', views.cinema_delete, name="cinema_delete"),
    path('cinema_update/delete/<int:pk>/', views.hall_delete, name="hall_delete"),
    path('cinema_update/hall_create/<int:pk>/', views.hall_create, name="hall_create"),
    path('cinema_update/<int:pk>/', views.cinema_update, name='cinema_update'),
    path('cinema_update/hall_update/<int:pk>/', views.hall_update, name='hall_update'),


]
