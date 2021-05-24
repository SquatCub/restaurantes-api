from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("restaurantes/", views.restaurantes_all, name="restaurantes"),
    path("restaurante/", views.restaurante, name="restaurante"),
    path("restaurante/crear", views.restaurante_create, name="crear"),
    path("restaurante/borrar/<str:id_restaurante>", views.restaurante_delete, name="eliminar"),
    path("restaurante/actualizar", views.restaurante_update, name="actualizar"),
    path("restaurantes/statistics", views.restaurantes_statistics, name="statistics")
]