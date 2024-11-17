from django.db import models

# los modelos versus tablas class

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='categorias/', null=True, blank=True)  # aquí imagen

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField()
    # campo categoria relacionada con tabla/class Categoria
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="productos")
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True) #aqui tambien 

    def __str__(self):
        return self.nombre