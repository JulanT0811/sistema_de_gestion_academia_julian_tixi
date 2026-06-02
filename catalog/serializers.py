from rest_framework import serializers
from .models import Curso, Estudiante

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    total_aprobados = serializers.SerializerMethodField()

    class Meta:
        model = Curso
        fields = ['id', 'codigo', 'nombre', 'total_aprobados']

    def get_total_aprobados(self, obj):
        return obj.estudiantes.filter(aprobado=True).count()