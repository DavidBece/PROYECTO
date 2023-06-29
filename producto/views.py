from django.shortcuts import render, redirect
from producto.models import Producto
from producto.forms import ProductoForm, ProductoUpdateForm
from producto.models import Marca
from producto.forms import MarcaForm, MarcaUpdateForm
from producto.models import Unidades
from producto.forms import UnidadesForm, UnidadesUpdateForm
from producto.models import Subcategoria
from producto.forms import SubcategoriaForm, SubcategoriaUpdateForm
from producto.models import Categoria
from producto.forms import CategoriaForm, CategoriaUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def producto_crear(request):
    titulo = "Producto"
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "El formulario se ha enviado correctamente.")
            return redirect("producto")
        else:
            messages.error(request, "El formulario tiene errores.")
    else:
        form = ProductoForm()
    context = {"titulo": titulo, "form": form}
    return render(request, "producto/producto/crear.html", context)


def producto_listar(request):
    titulo = "Producto"
    modulo = "Producto"
    productos = Producto.objects.all()
    context = {"titulo": titulo, "modulo": modulo, "productos": productos}
    return render(request, "producto/producto/listar.html", context)


def producto_modificar(request, pk):
    titulo = "Producto"
    producto = Producto.objects.get(id=pk)

    if request.method == "POST":
        form = ProductoUpdateForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, "El formulario se ha modificado correctamente.")
            return redirect("producto")
    else:
        form = ProductoUpdateForm(instance=producto)
    context = {"titulo": titulo, "form": form}
    return render(request, "producto/producto/modificar.html", context)


def producto_eliminar(request, pk):
    producto = Producto.objects.filter(id=pk)
    producto.update(estado="0")
    return redirect("producto")


def marca_crear(request):
    titulo = "Marca"
    if request.method == "POST":
        form = MarcaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "El formulario se ha enviado correctamente.")
            return redirect("marca")
        else:
            messages.error(request, "El formulario tiene errores.")
    else:
        form = MarcaForm()
    context = {"titulo": titulo, "form": form}
    return render(request, "producto/marca/crear.html", context)


def marca_listar(request):
    titulo = "Marca"
    modulo = "Producto"
    marcas = Marca.objects.all()
    context = {"titulo": titulo, "modulo": modulo, "marcas": marcas}
    return render(request, "producto/marca/listar.html", context)


def marca_modificar(request, pk):
    titulo = "Marca"
    marca = Marca.objects.get(id=pk)

    if request.method == "POST":
        form = MarcaUpdateForm(request.POST, instance=marca)
        if form.is_valid():
            form.save()
            messages.success(request, "El formulario se ha modificado correctamente.")
            return redirect("marca")
    else:
        form = MarcaUpdateForm(instance=marca)
    context = {"titulo": titulo, "form": form}
    return render(request, "producto/marca/modificar.html", context)


def marca_eliminar(request, pk):
    marca = Marca.objects.filter(id=pk)
    marca.update(estado="0")
    return redirect("marca")


def unidades_crear(request):
    titulo = "Unidades"
    if request.method == "POST":
        form = UnidadesForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "El formulario se ha enviado correctamente.")
            return redirect("unidades")
        else:
            messages.error(request, "El formulario tiene errores.")
    else:
        form = UnidadesForm()
    context = {"titulo": titulo, "form": form}
    return render(request, "producto/unidades/crear.html", context)


def unidades_listar(request):
    titulo = "Unidades"
    modulo = "Producto"
    unidades = Unidades.objects.all()
    context = {"titulo": titulo, "modulo": modulo, "unidades": unidades}
    return render(request, "producto/unidades/listar.html", context)


def unidades_modificar(request, pk):
    titulo = "Unidades"
    unidades = Unidades.objects.get(id=pk)

    if request.method == "POST":
        form = UnidadesUpdateForm(request.POST, instance=unidades)
        if form.is_valid():
            form.save()
            messages.success(request, "El formulario se ha modificado correctamente.")
            return redirect("unidades")
    else:
        form = UnidadesUpdateForm(instance=unidades)
    context = {"titulo": titulo, "form": form}
    return render(request, "producto/unidades/modificar.html", context)


def unidades_eliminar(request, pk):
    unidades = Unidades.objects.filter(id=pk)
    unidades.update(estado="0")
    return redirect("unidades")


def subcategoria_crear(request):
    titulo = "Subcategoria"
    if request.method == "POST":
        form = SubcategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "El formulario se ha enviado correctamente.")
            return redirect("subcategoria")
        else:
            messages.error(request, "El formulario tiene errores.")
    else:
        form = SubcategoriaForm()
    context = {"titulo": titulo, "form": form}
    return render(request, "producto/subcategoria/crear.html", context)


def subcategoria_listar(request):
    titulo = "Subcategoria"
    modulo = "Producto"
    subcategorias = Subcategoria.objects.all()
    context = {"titulo": titulo, "modulo": modulo, "subcategorias": subcategorias}
    return render(request, "producto/subcategoria/listar.html", context)


def subcategoria_modificar(request, pk):
    titulo = "Subcategoria"
    subcategoria = Subcategoria.objects.get(id=pk)

    if request.method == "POST":
        form = SubcategoriaUpdateForm(request.POST, instance=subcategoria)
        if form.is_valid():
            form.save()
            messages.success(request, "El formulario se ha modificado correctamente.")
            return redirect("subcategoria")
    else:
        form = SubcategoriaUpdateForm(instance=subcategoria)
    context = {"titulo": titulo, "form": form}
    return render(request, "producto/subcategoria/modificar.html", context)


def subcategoria_eliminar(request, pk):
    subcategoria = Subcategoria.objects.filter(id=pk)
    subcategoria.update(estado="0")
    return redirect("subcategoria")


def categoria_crear(request):
    titulo = "Categoria"
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("categoria")
    else:
        form = CategoriaForm()
    context = {"titulo": titulo, "form": form}
    return render(request, "producto/categoria/crear.html", context)


def categoria_listar(request):
    titulo = "Categoria"
    modulo = "Producto"
    categorias = Categoria.objects.all()
    context = {"titulo": titulo, "modulo": modulo, "categorias": categorias}
    return render(request, "producto/categoria/listar.html", context)


def categoria_modificar(request, pk):
    titulo = "Categoria"
    categoria = Categoria.objects.get(id=pk)

    if request.method == "POST":
        form = CategoriaUpdateForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, "El formulario se ha modificado correctamente.")
            return redirect("categoria")
    else:
        form = CategoriaUpdateForm(instance=categoria)
    context = {"titulo": titulo, "form": form}
    return render(request, "producto/categoria/modificar.html", context)


def categoria_eliminar(request, pk):
    categoria = Categoria.objects.filter(id=pk)
    categoria.update(estado="0")
    return redirect("categoria")
