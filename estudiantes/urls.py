from django.urls import path
from .views import MiHome, EstudianteLista, EstudianteView

urlpatterns = [
    path("home/", MiHome.as_view(), name='ver_home'),
    path("estudiantes/", EstudianteLista.as_view(), name='ver_estudiantes'),
    path("estudiante/<str:pk>", EstudianteView.as_view(), name='ver_estudiante'),
]
