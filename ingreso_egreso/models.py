from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from ventas.models import Venta
from compras.models import Compra
from producto.models import Producto
# Create your models here.
class Detalle_Venta(models.Model):
    nombre=models.ForeignKey(Producto, blank=True,verbose_name=_("Nombre"), on_delete=models.CASCADE)
    cantidad=models.CharField(max_length=10, blank=True,validators=[RegexValidator(r'^\d+$', message="Este campo solo permite números.")])
    venta=models.ForeignKey(Venta, blank=True,verbose_name=_("Venta"), on_delete=models.CASCADE)
    class Estado(models.TextChoices):
        ACTIVO="1",_("Activo")
        INACTIVO="2",_("Inactivo")
    estado=models.CharField(max_length=45,blank=True,verbose_name="Estado",choices=Estado.choices,default=Estado.ACTIVO)
    
    def __str__(self):
        return "%s"%(self.nombre)
    class Meta:
        verbose_name_plural = "Detalles de ventas"

class Detalle_Compra(models.Model):
    producto=models.ForeignKey(Producto, blank=True,verbose_name="Nombre", on_delete=models.CASCADE)
    precio_compra=models.PositiveIntegerField(max_length=45,blank=True,verbose_name="Precio de compra")
    precio_venta=models.PositiveIntegerField(max_length=45,blank=True,verbose_name="Precio de venta")
    compra=models.ForeignKey(Compra, verbose_name=_("Compra"),blank=True, on_delete=models.CASCADE)
    class Estado(models.TextChoices):
        ACTIVO="1",_("Activo")
        INACTIVO="2",_("Inactivo")
    estado=models.CharField(max_length=45,blank=True,verbose_name="Estado",choices=Estado.choices,default=Estado.ACTIVO)
    
    def __str__(self):
        return "%s"%(self.producto)
    class Meta:
        verbose_name_plural = "Detalles de compras"
class Stock(models.Model):
    cantidad=models.SmallIntegerField(max_length=45,blank=True,verbose_name="Cantidad")
    detalle_venta=models.ForeignKey(Detalle_Venta,blank=True, verbose_name=_("Detalle venta"), on_delete=models.CASCADE)
    detalle_compra=models.ForeignKey(Detalle_Compra,blank=True, verbose_name=_("Detalle compra"), on_delete=models.CASCADE)
    class Estado(models.TextChoices):
        ACTIVO="1",_("Activo")
        INACTIVO="2",_("Inactivo")
    estado=models.CharField(max_length=45,blank=True,verbose_name="Estado",choices=Estado.choices,default=Estado.ACTIVO)
    
    def __str__(self):
        return "%s"%(self.cantidad)
    class Meta:
        verbose_name_plural = "Stocks"