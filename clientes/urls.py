from django.urls import path
from . import views

urlpatterns = [
    path("buscar/", views.buscar_cliente_por_ruc, name="buscar_cliente_por_ruc"),
]
