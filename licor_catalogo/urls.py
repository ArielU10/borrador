from django.urls import path
from . import views

app_name = 'licor_catalogo'

urlpatterns = [
    path("", views.index, name="index"),

    # Categoria
    path("categorias/", views.categorias, name="categorias"),
    path("add_categoria/", views.add_categoria, name='add_categoria'),
    path("categorias/mostrar_categoria/<int:id>/", views.mostrar_categoria, name="mostrar_categoria"),
    path("categorias/edit_categoria/<int:id>/", views.edit_categoria, name='edit_categoria'),
    path("categorias/delete_categoria/<int:id>/", views.delete_categoria, name='delete_categoria'),

    # Producto
    path("productos/", views.productos, name="productos"),
    path("add_producto/", views.add_producto, name='add_producto'),
    path("productos/mostrar_producto/<int:id>/", views.mostrar_producto, name="mostrar_producto"),
    path("productos/edit_producto/<int:id>/", views.edit_producto, name='edit_producto'),
    path("productos/delete_producto/<int:id>/", views.delete_producto, name='delete_producto'),

    # Cliente
    path("clientes/", views.clientes, name="clientes"),
    path("add_cliente/", views.add_cliente, name='add_cliente'),
    path("clientes/mostrar_cliente/<int:id>/", views.mostrar_cliente, name="mostrar_cliente"),
    path("clientes/edit_cliente/<int:id>/", views.edit_cliente, name='edit_cliente'),
    path("clientes/delete_cliente/<int:id>/", views.delete_cliente, name='delete_cliente'),

    # Compra
    path("compras/", views.compras, name="compras"),
    path("add_compra/", views.add_compra, name='add_compra'),
    path("compras/mostrar_compra/<int:id>/", views.mostrar_compra, name="mostrar_compra"),

    path("login/", views.CustomLoginView.as_view(), name='login'),
]
