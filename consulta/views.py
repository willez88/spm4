from django.shortcuts import render

# Create your views here.

def parametros(request):
    return render(request, 'consulta.parametros.template.html')
