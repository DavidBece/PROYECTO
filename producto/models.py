from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
# Create your models here.

class Marca(models.Model):
    marca=models.CharField(max_length=45,blank=True,verbose_name="Marca")
    
    class Estado(models.TextChoices):
        ACTIVO="1",_("Activo")
        INACTIVO="2",_("Inactivo")
    estado=models.CharField(max_length=45,blank=True,verbose_name="Estado",choices=Estado.choices,default=Estado.ACTIVO)
    
    def __str__(self):
        return "%s"%(self.marca)
    class Meta:
        verbose_name_plural = "Marcas"

class Unidades(models.Model):
    unidades=models.CharField(max_length=10, blank=True,validators=[RegexValidator(r'^\d+$', message="Este campo solo permite números.")])
    class Medida(models.TextChoices):
        pulgada="1",_("Pulgada")
        centimetro="2",_("Centimetro")
        milimetros="3",_("Milimetros")
        kilos="4",_("Kilos")
        miligramos="5",_("Miligramos")       
        libras="6",_("Libras")
    medida=models.CharField(max_length=45,blank=True,verbose_name="Medida",choices=Medida.choices)
    class Estado(models.TextChoices):
        ACTIVO="1",_("Activo")
        INACTIVO="2",_("Inactivo")
    estado=models.CharField(max_length=45,blank=True,verbose_name="Estado",choices=Estado.choices,default=Estado.ACTIVO)
    def __str__(self):
        return "%s"%(self.unidades)
    class Meta:
        verbose_name_plural = "Unidades"

class Subcategoria(models.Model):
    class Subcategory(models.TextChoices):
        construccion="Construccion",_("Construcción")
        electricidad="Electricidad",_("Electricidad")
        herramientas_manual="Herramientas Manual",_("Herramientas Manual")
        plomeria_tuberias="Plomeria y Tuberias",_("Plomeria y Tuberias")
    subcategoria=models.CharField(max_length=45,blank=True,verbose_name="Subcategoria",choices=Subcategory.choices)
    class Estado(models.TextChoices):
        ACTIVO="1",_("Activo")
        INACTIVO="2",_("Inactivo")
    estado=models.CharField(max_length=45,blank=True,verbose_name="Estado",choices=Estado.choices,default=Estado.ACTIVO)
    def __str__(self):
        return "%s"%(self.subcategoria)
    class Meta:
        verbose_name_plural = "Subcategorias"

class Categoria(models.Model):
    nombre=models.CharField(max_length=45,blank=True,validators=[RegexValidator(r'^[A-Za-z]+$', message="Este campo solo permite letras.")])
    subcategoria=models.ForeignKey(Subcategoria,blank=True,on_delete=models.CASCADE)
    class Estado(models.TextChoices):
        ACTIVO="1",_("Activo")
        INACTIVO="2",_("Inactivo")
    estado=models.CharField(max_length=45,blank=True,verbose_name="Estado",choices=Estado.choices,default=Estado.ACTIVO)

    def __str__(self):
        return "%s"%(self.nombre)
    class Meta:
        verbose_name_plural = "Categorias"



class Producto(models.Model):
    nombre=models.CharField(max_length=45,blank=True,validators=[RegexValidator(r'^[A-Za-z]+$', message="Este campo solo permite letras.")])
    precio=models.CharField(max_length=45,blank=True,verbose_name="Precio",validators=[RegexValidator(r'^\d+$', message="Este campo solo permite números.")])
    
    class Color(models.TextChoices):
        azul="1",_("Azul")
        rojo="2",_("Rojo")
        amarillo="3",_("Amarillo")
        verde="4",_("Verde")
        negro="5",_("Negro")
    color=models.CharField(max_length=45,blank=True,verbose_name="Color",choices=Color.choices)
    class Presentacion(models.TextChoices):
        bolsa="1",_("Bolsa")
        caja="2",_("Caja")
    presentacion=models.CharField(max_length=45,blank=True,verbose_name="Presentacion",choices=Presentacion.choices)
    class Material(models.TextChoices):
        metal="1",_("Metal")
        plastico="2",_("Plastico")
        hierro="3",_("Hierro")
    material=models.CharField(max_length=45,blank=True,verbose_name="Material",choices=Material.choices)
    marca= models.ForeignKey(Marca, related_name='Marca',blank=True, on_delete=models.CASCADE)
    unidades= models.ForeignKey(Unidades, related_name='Unidades', blank=True,on_delete=models.CASCADE)
    categoria= models.ForeignKey(Categoria, related_name='Categoria', blank=True,on_delete=models.CASCADE)
    class Estado(models.TextChoices):
        ACTIVO="1",_("Activo")
        INACTIVO="2",_("Inactivo")
    estado=models.CharField(max_length=45, blank=True,verbose_name="Estado",choices=Estado.choices,default=Estado.ACTIVO)
    
    def clean(self):
        self.nombre=self.nombre.title()
    def __str__(self):
        return "%s"%(self.nombre)
    class Meta:
        verbose_name_plural = "Productos"




