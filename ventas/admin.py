from django.contrib import admin
from .models import Producto, Venta, DetalleVenta

class DetalleVentaInline(admin.TabularInline):
    model = DetalleVenta
    extra = 1

    # Calcula el subtotal antes de guardar
    def save_model(self, request, obj, form, change):
        if obj.producto and obj.cantidad:
            obj.subtotal = obj.producto.precio * obj.cantidad
        super().save_model(request, obj, form, change)

class VentaAdmin(admin.ModelAdmin):
    inlines = [DetalleVentaInline]

    # Calcula el total después de guardar los detalles
    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        venta = form.instance
        total = 0
        for detalle in venta.detalles.all():  # ✅ Usar related_name correcto
            total += detalle.subtotal or 0
        venta.total = total
        venta.save()

admin.site.register(Producto)
admin.site.register(Venta, VentaAdmin)
