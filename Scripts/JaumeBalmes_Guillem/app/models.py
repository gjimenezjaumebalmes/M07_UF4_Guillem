from django.db import models

class Profesor(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100)
    asignatura = models.CharField(max_length=100)
    email = models.EmailField()
    curso = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
