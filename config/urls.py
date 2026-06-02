from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from catalog.views import CursoViewSet, EstudianteViewSet, CalcularNotasView, ProgramarModulosView

router = DefaultRouter()
router.register(r'cursos', CursoViewSet)
router.register(r'estudiantes', EstudianteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/academia/notas/', CalcularNotasView.as_view()),
    path('api/academia/modulos/', ProgramarModulosView.as_view()),
]