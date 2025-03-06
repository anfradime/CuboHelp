from django.db import models

class Ticket(models.Model):
    STATUS_CHOICES = [
        ('abierto', 'Abierto'),
        ('en_progreso', 'En Progreso'),
        ('cerrado', 'Cerrado'),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    estado = models.CharField(max_length=20, choices=STATUS_CHOICES, default='abierto')
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo