from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MarcaViewSet, VehiculoViewSet
from .estudiantes_types_views import cursos_types_list_create, cursos_types_detail
from .estudiantes_views import estudiantes_services_list_create, estudiantes_services_detail

router = DefaultRouter()
router.register(r"cursos", MarcaViewSet, basename="cursos")
router.register(r"estudiantes", VehiculoViewSet, basename="estudiantes")

urlpatterns = [
    # Mongo
    path("cursos-types/", cursos_types_list_create),
    path("cursos-types//", cursos_types_detail),
    path("estudiantes-services/", estudiantes_services_list_create),
    path("estudiantes-services//", estudiantes_services_detail),
]

urlpatterns += router.urls