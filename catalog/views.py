from rest_framework import viewsets
from .models import Curso, Estudiante
from .serializers import CursoSerializer, EstudianteSerializer
from .permissions import IsAdminOrReadOnly

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    permission_classes = [IsAdminOrReadOnly]

class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer
    permission_classes = [IsAdminOrReadOnly]