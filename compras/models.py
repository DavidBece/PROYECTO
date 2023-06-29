from django.db import models
from usuarios.models import Usuario
from producto.models import Producto
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator


# Create your models here.

        
class Cuenta_Pendiente(models.Model):
    nombre=models.CharField(max_length=45,blank=True,validators=[RegexValidator(r'^[A-Za-z]+$', message="Este campo solo permite letras.")])
    nombre_producto = models.ForeignKey(Producto, blank=True,verbose_name=_("Nombre del Producto"), on_delete=models.CASCADE)
    fecha_inicio=models.DateField(verbose_name="Fecha de Inicio", blank=True,help_text="MM/DD/AAAA", auto_now=True)
    valor=models.IntegerField(max_length=45,blank=True,verbose_name="Valor")
    class Estado(models.TextChoices):
        ACTIVO="1",_("Activo")
        INACTIVO="2",_("Inactivo")
    estado=models.CharField(max_length=15,blank=True,verbose_name="Estado",choices=Estado.choices,default=Estado.ACTIVO)
    def __str__(self):
        return "%s"%(self.nombre)
    class Meta:
        verbose_name_plural = "Cuentas Pendientes"


class Compra(models.Model):
    fecha=models.DateField(verbose_name="Fecha", blank=True,help_text="MM/DD/AAAA", auto_now=True)
    idusuario=models.ForeignKey(Usuario, blank=True,verbose_name=_("Usuario"), on_delete=models.CASCADE)
    idcuentapendiente=models.ForeignKey(Cuenta_Pendiente,blank=True, verbose_name=_("Cuenta Pendiente"), on_delete=models.CASCADE)
    class Estado(models.TextChoices):
        ACTIVO="1",_("Activo")
        INACTIVO="2",_("Inactivo")
    estado=models.CharField(max_length=15,blank=True,verbose_name="Estado",choices=Estado.choices,default=Estado.ACTIVO)
    def __str__(self):
        return "%s %s"%(self.fecha,self.estado)
    class Meta:
        verbose_name_plural = "Compras"