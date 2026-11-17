from django.urls import path
from . import views

urlpatterns = [
    path("", views.produto_lista, name="produto_lista"),
    path("produtos/novo/", views.produto_criar, name="produto_criar"),
    path("produtos/<int:pk>/editar/", views.produto_editar, name="produto_editar"),
]
