from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Estudiante
from django.http import Http404

class MiHome(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contexto"] = {
            "nombres": ["Juan", "María", "Pedro"],
            "valido": False,
            "fecha": '02-07-2024'
        }
        return context

class EstudianteLista(ListView):
    model = Estudiante
    template_name = 'estudiantes.html'
    context_object_name = 'lista_estudiantes'

class EstudianteView(DetailView):
    model = Estudiante
    template_name = "estudiante.html"
    context_object_name = 'alumno'

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Http404:
            return None
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if self.object is None:
            context['error'] = 'Estudiante no encontrado'
        
        return context
    