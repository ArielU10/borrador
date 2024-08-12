from django.contrib import admin
from .models import Categoria, Producto, Cliente, Compra

# Registro de los modelos en el administrador de Django

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'stock')
    search_fields = ('nombre', 'categoria__nombre')
    list_filter = ('categoria',)
    ordering = ('nombre',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'fecha_registro')
    search_fields = ('nombre', 'email')
    ordering = ('fecha_registro',)

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'producto', 'cantidad', 'fecha_compra', 'total')
    search_fields = ('cliente__nombre', 'producto__nombre')
    list_filter = ('fecha_compra',)
    ordering = ('fecha_compra',)
