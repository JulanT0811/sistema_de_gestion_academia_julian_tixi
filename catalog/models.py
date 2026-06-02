from django.db import models

class Curso(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    curso = models.ForeignKey(Curso, related_name='estudiantes', on_delete=models.PROTECT)
    nombre = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)
    nota_parcial = models.DecimalField(max_digits=5, decimal_places=2)
    nota_final = models.DecimalField(max_digits=5, decimal_places=2)
    aprobado = models.BooleanField(default=False)