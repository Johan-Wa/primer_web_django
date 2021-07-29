from django.db import models



# Create your models here.

class CategoriaProd(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'categororiaProd'
        verbose_name_plural = 'categoriasProd'

    def __str__(self) -> str:
        return self.name

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    categorias = models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to="tienda", null=True, blank=True)
    disponibilidad = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'porducto'
        verbose_name_plural = 'productos'

    def __str__(self) -> str:
        return self.nombre
        