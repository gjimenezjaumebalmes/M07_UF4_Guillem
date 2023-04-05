from django.db import models


class Profesor(models.Model):

    id = models.IntegerField(primary_key=True)
    nombre = models.TextField()
    asignatura = models.TextField()
    email = models.TextField()
    curso = models.CharField(max_length=50, null=True, default=None)

class Alumno(models.Model):

    id = models.IntegerField(primary_key=True)
    nombre = models.TextField()
    curso = models.CharField(max_length=50, null=True, default=None)
    email = models.TextField()
