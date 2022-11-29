from django.db import models

# Create your models here. escribir Model y tab
class Persona(models.Model):
    nombre = models.CharField("Nombre completo", max_length=100)
    descripcion = models.TextField("Descripción")
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'MODELNAME'
        verbose_name_plural = 'MODELNAMEs'

    def __str__(self):
        return self.nombre
        pass

