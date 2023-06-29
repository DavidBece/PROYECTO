from django.shortcuts import render, redirect
from usuarios.models import Usuario
from usuarios.forms import UsuarioForm, UsuarioUpdateForm
from usuarios.models import Sucursal
from usuarios.forms import SucursalForm, SucursalUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def usuario_crear(request):
    titulo = "Usuario"
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "El formulario se ha enviado correctamente.")
            return redirect("usuario")
        else:
            messages.error(request, "El formulario tiene errores.")
    else:
        form = UsuarioForm()
    context = {"titulo": titulo, "form": form}
    return render(request, "usuarios/usuarios/crear.html", context)


def usuario_listar(request):
    titulo = "Usuario"
    modulo = "Usuarios"
    usuarios = Usuario.objects.all()
    context = {"titulo": titulo, "modulo": modulo, "usuarios": usuarios}
    return render(request, "usuarios/usuarios/listar.html", context)


def usuario_modificar(request, pk):
    titulo = "Usuario"
    usuario = Usuario.objects.get(id=pk)

    if request.method == "POST":
        form = UsuarioUpdateForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, "El formulario se ha modificado correctamente.")
            return redirect("usuario")
    else:
        form = UsuarioUpdateForm(instance=usuario)
    context = {"titulo": titulo, "form": form}
    return render(request, "usuarios/usuarios/modificar.html", context)


def usuario_eliminar(request, pk):
    usuario = Usuario.objects.filter(id=pk)
    usuario.update(estado="0")
    return redirect("usuario")


def sucursal_crear(request):
    titulo = "Sucursal"
    if request.method == "POST":
        form = SucursalForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "El formulario se ha enviado correctamente.")
            return redirect("sucursal")
    else:
        form = SucursalForm()
    context = {"titulo": titulo, "form": form}
    return render(request, "usuarios/sucursal/crear.html", context)


def sucursal_listar(request):
    titulo = "Sucursal"
    modulo = "Usuarios"
    sucursales = Sucursal.objects.all()
    context = {"titulo": titulo, "modulo": modulo, "sucursales": sucursales}
    return render(request, "usuarios/sucursal/listar.html", context)


def sucursal_modificar(request, pk):
    titulo = "Sucursal"
    sucursal = Sucursal.objects.get(id=pk)

    if request.method == "POST":
        form = SucursalUpdateForm(request.POST, instance=sucursal)
        if form.is_valid():
            form.save()
            messages.success(request, "El formulario se ha modificado correctamente.")
            return redirect("sucursal")
    else:
        form = SucursalUpdateForm(instance=sucursal)
    context = {"titulo": titulo, "form": form}
    return render(request, "usuarios/sucursal/modificar.html", context)


def sucursal_eliminar(request, pk):
    sucursal = Sucursal.objects.filter(id=pk)
    sucursal.update(estado="0")
    return redirect("sucursal")
