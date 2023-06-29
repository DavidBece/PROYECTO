from django.shortcuts import render, redirect
from ingreso_egreso.models import Stock
from ingreso_egreso.forms import StockForm, StockUpdateForm
from ingreso_egreso.models import Detalle_Compra
from ingreso_egreso.forms import Detalle_CompraForm, Detalle_CompraUpdateForm
from ingreso_egreso.models import Detalle_Venta
from ingreso_egreso.forms import Detalle_VentaForm, Detalle_VentaUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def stock_crear(request):
    titulo = "Stock"
    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "El formulario se ha enviado correctamente.")
            return redirect("stock")
        else:
            messages.error(request, "El formulario tiene errores.")
    else:
        form = StockForm()
    context = {"titulo": titulo, "form": form}
    return render(request, "ingreso_egreso/stock/crear.html", context)


def stock_listar(request):
    titulo = "Stock"
    modulo = "Ingreso_egreso"
    stocks = Stock.objects.all()
    context = {"titulo": titulo, "modulo": modulo, "stocks": stocks}
    return render(request, "ingreso_egreso/stock/listar.html", context)


def stock_modificar(request, pk):
    titulo = "Stock"
    stock = Stock.objects.get(id=pk)

    if request.method == "POST":
        form = StockUpdateForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            messages.success(request, "El formulario se ha modificado correctamente.")
            return redirect("stock")
    else:
        form = StockUpdateForm(instance=stock)
    context = {"titulo": titulo, "form": form}
    return render(request, "ingreso_egreso/stock/modificar.html", context)


def stock_eliminar(request, pk):
    stock = Stock.objects.filter(id=pk)
    stock.update(estado="0")
    return redirect("stock")


def detalle_compra_crear(request):
    titulo = "Detalle Compra"
    if request.method == "POST":
        form = Detalle_CompraForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "El formulario se ha enviado correctamente.")
            return redirect("detalle_compra")
        else:
            messages.error(request, "El formulario tiene errores.")
    else:
        form = Detalle_CompraForm()
    context = {"titulo": titulo, "form": form}
    return render(request, "ingreso_egreso/detalle_compra/crear.html", context)


def detalle_compra_listar(request):
    titulo = "Detalle Compra"
    modulo = "Ingreso_egreso"
    detalle_compras = Detalle_Compra.objects.all()
    context = {"titulo": titulo, "modulo": modulo, "detalle_compras": detalle_compras}
    return render(request, "ingreso_egreso/detalle_compra/listar.html", context)


def detalle_compra_modificar(request, pk):
    titulo = "Detalle Compra"
    detalle_compra = Detalle_Compra.objects.get(id=pk)

    if request.method == "POST":
        form = Detalle_CompraUpdateForm(request.POST, instance=detalle_compra)
        if form.is_valid():
            form.save()
            messages.success(request, "El formulario se ha modificado correctamente.")
            return redirect("detalle_compra")
    else:
        form = Detalle_CompraUpdateForm(instance=detalle_compra)
    context = {"titulo": titulo, "form": form}
    return render(request, "ingreso_egreso/detalle_compra/modificar.html", context)


def detalle_compra_eliminar(request, pk):
    detalle_compra = Detalle_Compra.objects.filter(id=pk)
    detalle_compra.update(estado="0")
    return redirect("detalle_compra")


def detalle_venta_crear(request):
    titulo = "Detalle Venta"
    if request.method == "POST":
        form = Detalle_VentaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "El formulario se ha enviado correctamente.")
            return redirect("detalle_venta")
        else:
            messages.error(request, "El formulario tiene errores.")
    else:
        form = Detalle_VentaForm()
    context = {"titulo": titulo, "form": form}
    return render(request, "ingreso_egreso/detalle_venta/crear.html", context)


def detalle_venta_listar(request):
    titulo = "Detalle Venta"
    modulo = "Ingreso_egreso"
    detalle_ventas = Detalle_Venta.objects.all()
    context = {"titulo": titulo, "modulo": modulo, "detalle_ventas": detalle_ventas}
    return render(request, "ingreso_egreso/detalle_venta/listar.html", context)


def detalle_venta_modificar(request, pk):
    titulo = "Detalle Venta"
    detalle_venta = Detalle_Venta.objects.get(id=pk)

    if request.method == "POST":
        form = Detalle_VentaUpdateForm(request.POST, instance=detalle_venta)
        if form.is_valid():
            form.save()
            messages.success(request, "El formulario se ha modificado correctamente.")
            return redirect("detalle_venta")
    else:
        form = Detalle_VentaUpdateForm(instance=detalle_venta)
    context = {"titulo": titulo, "form": form}
    return render(request, "ingreso_egreso/detalle_venta/modificar.html", context)


def detalle_venta_eliminar(request, pk):
    detalle_venta = Detalle_Venta.objects.filter(id=pk)
    detalle_venta.update(estado="0")
    return redirect("detalle_venta")
