from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class InicioView(TemplateView):
    template_name = "base.template.html"
