# ventas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.productos_list, name='productos_list'),
    path('productos/add/', views.producto_add, name='producto_add'),
    path('productos/edit/<int:producto_id>/', views.producto_edit, name='producto_edit'),
    path('productos/delete/<int:producto_id>/', views.producto_delete, name='producto_delete'),

    path('ventas/add/', views.venta_add, name='venta_add'),
    path('ventas/', views.ventas_list, name='ventas_list'),
    path('ventas/<int:venta_id>/', views.venta_detail, name='venta_detail'),

    # ✅ PDF de todas las ventas
    path('ventas/pdf/', views.ventas_pdf, name='ventas_pdf'),

    # ✅ PDF de una factura
    path('factura/<int:venta_id>/', views.factura_pdf, name='factura_pdf'),
]
