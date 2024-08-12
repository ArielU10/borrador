from django.shortcuts import get_object_or_404, redirect, render

from .models import Categoria, Producto, Cliente, Compra
from .forms import CategoriaForm, ProductoForm, ClienteForm, CompraForm

from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

# Vista de inicio
def index(request):
    return render(request, 'index.html')

# Categorías
def categorias(request):
    categorias = Categoria.objects.all()
    context = {
        'categorias': categorias
    }
    return render(request, 'categorias.html', context)

def mostrar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    context = {
        'categoria': categoria
    }
    return render(request, 'categoria_details.html', context)

@login_required
def add_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('licor_catalogo:categorias')
    else:
        form = CategoriaForm()
    
    return render(request, 'categoria_form.html', {'form': form})

@login_required
def edit_categoria(request, id):
    categoria = get_object_or_404(Categoria, pk=id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, request.FILES, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('licor_catalogo:categorias')
    else:
        form = CategoriaForm(instance=categoria)
    
    return render(request, 'categoria_form.html', {'form': form})

@login_required
def delete_categoria(request, id):
    categoria = get_object_or_404(Categoria, pk=id)
    categoria.delete()
    return redirect('licor_catalogo:categorias')

# Productos
def productos(request):
    productos = Producto.objects.all()
    context = {
        'productos': productos
    }
    return render(request, 'productos.html', context)

def mostrar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    context = {
        'producto': producto
    }
    return render(request, 'producto_details.html', context)

@login_required
def add_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('licor_catalogo:productos')
    else:
        form = ProductoForm()
    
    return render(request, 'producto_form.html', {'form': form})

@login_required
def edit_producto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('licor_catalogo:productos')
    else:
        form = ProductoForm(instance=producto)
    
    return render(request, 'producto_form.html', {'form': form})

@login_required
def delete_producto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    producto.delete()
    return redirect('licor_catalogo:productos')

# Clientes
def clientes(request):
    clientes = Cliente.objects.all()
    context = {
        'clientes': clientes
    }
    return render(request, 'clientes.html', context)

def mostrar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    context = {
        'cliente': cliente
    }
    return render(request, 'cliente_details.html', context)

@login_required
def add_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('licor_catalogo:clientes')
    else:
        form = ClienteForm()
    
    return render(request, 'cliente_form.html', {'form': form})

@login_required
def edit_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('licor_catalogo:clientes')
    else:
        form = ClienteForm(instance=cliente)
    
    return render(request, 'cliente_form.html', {'form': form})

@login_required
def delete_cliente(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    cliente.delete()
    return redirect('licor_catalogo:clientes')

# Compras (No se permite editar ni eliminar)
def compras(request):
    compras = Compra.objects.all()
    context = {
        'compras': compras
    }
    return render(request, 'compras.html', context)

def mostrar_compra(request, id):
    compra = get_object_or_404(Compra, id=id)
    context = {
        'compra': compra
    }
    return render(request, 'compra_details.html', context)

@login_required
def add_compra(request):
    if request.method == 'POST':
        form = CompraForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('licor_catalogo:compras')
    else:
        form = CompraForm()
    
    return render(request, 'compra_form.html', {'form': form})

# Custom login view
class CustomLoginView(LoginView):
    template_name = 'login.html'

