from django.shortcuts import render, redirect
from compras.models import Compra
from compras.forms import CompraForm, CompraUpdateForm
from compras.models import Cuenta_Pendiente
from compras.forms import Cuenta_PendienteForm, Cuenta_PendienteUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def compra_crear(request):
    titulo = "Compra"
    if request.method == "POST":
        form = CompraForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "El formulario se ha enviado correctamente.")
            return redirect("compra")
        else:
            messages.error(request, "El formulario tiene errores.")
    else:
        form = CompraForm()
    context = {"titulo": titulo, "form": form}
    return render(request, "compras/compras/crear.html", context)


def compra_listar(request):
    titulo = "Compra"
    modulo = "Compras"
    compras = Compra.objects.all()
    context = {"titulo": titulo, "modulo": modulo, "compras": compras}
    return render(request, "compras/compras/listar.html", context)


def compra_modificar(request, pk):
    titulo = "Compra"
    compra = Compra.objects.get(id=pk)

    if request.method == "POST":
        form = CompraUpdateForm(request.POST, instance=compra)
        if form.is_valid():
            form.save()
            messages.success(request, "El formulario se ha modificado correctamente.")
            return redirect("compra")
    else:
        form = CompraUpdateForm(instance=compra)
    context = {"titulo": titulo, "form": form}
    return render(request, "compras/compras/modificar.html", context)


def compra_eliminar(request, pk):
    compra = Compra.objects.filter(id=pk)
    compra.update(estado="0")
    return redirect("compra")


def cuenta_pendiente_crear(request):
    titulo = "Cuenta Pendiente"
    if request.method == "POST":
        form = Cuenta_PendienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "El formulario se ha enviado correctamente.")
            return redirect("cuenta_pendiente")
        else:
            messages.error(request, "El formulario tiene errores.")
    else:
        form = Cuenta_PendienteForm()
    context = {"titulo": titulo, "form": form}
    return render(request, "compras/cuentaspendientes/crear.html", context)


def cuenta_pendiente_listar(request):
    titulo = "Cuenta Pendiente"
    modulo = "Compras"
    cuentaspendientes = Cuenta_Pendiente.objects.all()
    context = {
        "titulo": titulo,
        "modulo": modulo,
        "cuentaspendientes": cuentaspendientes,
    }
    return render(request, "compras/cuentaspendientes/listar.html", context)


def cuenta_pendiente_modificar(request, pk):
    titulo = "Cuenta Pendiente"
    cuentapendiente = Cuenta_Pendiente.objects.get(id=pk)

    if request.method == "POST":
        form = Cuenta_PendienteUpdateForm(request.POST, instance=cuentapendiente)
        if form.is_valid():
            form.save()
            messages.success(request, "El formulario se ha modificado correctamente.")
            return redirect("cuenta_pendiente")
    else:
        form = Cuenta_PendienteUpdateForm(instance=cuentapendiente)
    context = {"titulo": titulo, "form": form}
    return render(request, "compras/cuentaspendientes/modificar.html", context)


def cuenta_pendiente_eliminar(request, pk):
    cuentapendiente = Cuenta_Pendiente.objects.filter(id=pk)
    cuentapendiente.update(estado="0")
    return redirect("cuenta_pendiente")
