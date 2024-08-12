from django.db import models

# Modelo para Categorías de licores
class Categoria(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.nombre

# Modelo para Productos de licores
class Producto(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    descripcion = models.TextField(null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0, null=False)
    imagen = models.ImageField(upload_to='productos_imagenes', null=True, blank=True)

    def __str__(self) -> str:
        return self.nombre

# Modelo para Clientes
class Cliente(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    email = models.EmailField(unique=True, null=False)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.nombre

# Modelo para Compras
class Compra(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=False, default=1)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    def __str__(self) -> str:
        return f"Compra de {self.cantidad}x {self.producto.nombre} por {self.cliente.nombre}"
