from django.db import models
from django.contrib.auth.models import User
from clientes.models import Cliente
from cloudinary.models import CloudinaryField

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    categoria = models.CharField(max_length=50, blank=True, null=True)
    imagen = CloudinaryField('image', blank=True, null=True)
    
    def __str__(self):
        return self.nombre

class Venta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True, blank=True, related_name='ventas')
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"Venta #{self.id} - {self.fecha.strftime('%Y-%m-%d %H:%M')}"

    def calcular_total(self):
        total = sum(detalle.subtotal for detalle in self.detalles.all() if detalle.subtotal)
        self.total = total
        self.save()


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name="detalles")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Calcular subtotal automáticamente
        if self.producto and self.cantidad:
            self.subtotal = self.producto.precio * self.cantidad

        # Si es una nueva creación, descontar stock
        if self.pk is None:
            if self.producto.stock >= self.cantidad:
                self.producto.stock -= self.cantidad
                self.producto.save()
            else:
                raise ValueError(f"Stock insuficiente para el producto {self.producto.nombre}")

        super().save(*args, **kwargs)

        # Actualizar el total de la venta
        if self.venta:
            self.venta.calcular_total()

    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad}"
