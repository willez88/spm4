from django.shortcuts import render
from .models import Persona, Persona2
from mongoengine.queryset.visitor import Q

# Create your views here.

def parametros(request):
    persona2 = Persona2(nombre="William",apellido="Páez",cedula="19102678",edad=28)
    persona2.save()

    persona2= Persona2.objects
    #print(persona2)
    #for p in Persona.objects.filter( Q(edad__gt=25) | Q(edad__lt=28) ):
    #    print(p.nombre)

    #for p in Persona.objects.filter( __raw__={'edad': {'$gt':25}} ):
    #    print(p.nombres)
    return render(request, 'consulta.parametros.template.html')

def resultado_parametros(request):
    if request.method == "POST":
        print(request.POST['spmid_1'])
        print(request.POST['spmid_2'])

    return render(request, 'consulta.resultados.parametros.html')
