from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.core.validators import EmailValidator
# Create your models here.
class Usuario(models.Model):
    nombre =models.CharField(max_length=45,unique=True, blank=True,validators=[RegexValidator(r'^[A-Za-z]+$', message="Este campo solo permite letras.")])
    apellido=models.CharField(max_length=45,blank=True,validators=[RegexValidator(r'^[A-Za-z]+$', message="Este campo solo permite letras.")])
    contraseña=models.CharField(max_length=45,blank=True,verbose_name="Contraseña")
    class TipoDocumento(models.TextChoices):
        CEDULA='CC',_("Cédula Ciudadania")
        TARJETA='TI',_("Tarjeta de Identidad")
        CEDULA_EXTRANJERIA='CE',_("Cédula de Extrangería")
    tipo_documento=models.CharField(max_length=2,blank=True,choices=TipoDocumento.choices,verbose_name="Tipo de Documento")
    documento=models.CharField(max_length=10, blank=True,validators=[RegexValidator(r'^\d+$', message="Este campo solo permite números.")])
    telefono=models.CharField(max_length=13, blank=True,validators=[RegexValidator(r'^\d+$', message="Este campo solo permite números.")])
    direccion=models.CharField(max_length=15,blank=True,verbose_name="Dirección")
    correo=models.EmailField(blank=True,validators=[EmailValidator(message="Por favor, ingresa una dirección de correo electrónico válida.")])
    class Rol(models.TextChoices):
        ADMIN='Admin',_("Administrador")
        EMPLEADO='Empleado',_("Empleado")
        USUARIO='Usuario',_("Usuario")
    rol=models.CharField(max_length=10,choices=Rol.choices,blank=True,verbose_name="Rol")
    class Estado(models.TextChoices):
        ACTIVO="1",_("Activo")
        INACTIVO="2",_("Inactivo")
    estado=models.CharField(max_length=45,verbose_name="Estado",blank=True,choices=Estado.choices,default=Estado.ACTIVO)
    def __str__(self):
        return "%s %s"%(self.nombre, self.apellido)
    class Meta:
        verbose_name_plural = "Usuarios"

class Sucursal(models.Model):
    nombre = models.CharField(max_length=45,blank=True,validators=[RegexValidator(r'^[A-Za-z]+$', message="Este campo solo permite letras.")])
    direccion=models.CharField(max_length=45,blank=True,verbose_name="Dirección")
    municipio=models.CharField(max_length=45,blank=True,validators=[RegexValidator(r'^[A-Za-z]+$', message="Este campo solo permite letras.")])
    telefono=models.CharField(max_length=10, blank=True,validators=[RegexValidator(r'^\d+$', message="Este campo solo permite números.")])
    class Estado(models.TextChoices):
        ACTIVO="1",_("Activo")
        INACTIVO="2",_("Inactivo")
    estado=models.CharField(max_length=45,blank=True,verbose_name="Estado",choices=Estado.choices,default=Estado.ACTIVO)
    def __str__(self):
        return "%s %s"%(self.nombre,self.municipio)
    class Meta:
        verbose_name_plural = "Sucursales"
class Usuario_has_Sucursal(models.Model):
    idusuario=models.ForeignKey(Usuario, verbose_name=_("ID Usuario"), on_delete=models.CASCADE)
    idsucursal=models.ForeignKey(Sucursal, verbose_name=_("ID Sucursal"), on_delete=models.CASCADE)