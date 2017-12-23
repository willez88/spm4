from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .forms import ParametroForm
from .models import Persona, Estrella
from mongoengine.queryset.visitor import Q

# Create your views here.

def parametros(request):
    #persona2 = Persona2(nombre="William",apellido="Páez",cedula="19102678",edad=28)
    #persona2.save()

    #prueba
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

class ParametroView(FormView):
    template_name = 'consulta.parametros.template.html'
    form_class = ParametroForm
    #success_url = reverse_lazy('resultado')

    def form_valid(self, form):
        spmid_operador = form.cleaned_data['spmid_operador']
        spmid = form.cleaned_data['spmid']
        operador_logico_1 = form.cleaned_data['operador_logico_1']

        if spmid != '' and ra != '':
            print("Si or o and")

        if spmid == '':
            print("No or o and")
        if ra == '':
            print("")



        c = 0
        for fo in form.cleaned_data:
            if form.cleaned_data[fo] == 'and':
                c = c + 1

        print(c)

        prueba = {'ra': {'$lt':0}}
        print(prueba)
        estrella = Estrella.objects.filter(
            __raw__= prueba
                #'ra': {'$lt': 30},
                #'dec': {'$lt': 30},
                #'$or': [{'b': {'$lt': 30}}, {'v': {"$lt": 30}}]
        )

        print(estrella)
        return render(self.request, 'consulta.resultado.html', {'spmid':spmid,'spmid_operador':spmid_operador})
        #return super(ParametroView, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super(ParametroView, self).form_invalid(form)

class ResultadoView(TemplateView):
    template_name = 'consulta.resultado.html'

class DatosPruebaView(TemplateView):
    template_name = 'consulta.datos.prueba.html'
    def get_context_data(self, **kwargs):
        context = super(DatosPruebaView, self).get_context_data(**kwargs)
        c = 0
        archivo = open('/media/william/565C935D5C933729/Documents and Settings/William/Downloads/Ubuntu/rs.asc', 'r')
        for linea in archivo:
            lista = linea.split(' ')
            estrella = Estrella()
            estrella.ra = float(lista[0])
            estrella.dec = float(lista[1])
            estrella.era = float(lista[2])
            estrella.edec = float(lista[3])
            estrella.pma = float(lista[4])
            estrella.pmd = float(lista[5])
            estrella.epma = float(lista[6])
            estrella.empd = float(lista[7])
            estrella.b = float(lista[8])
            estrella.v = float(lista[9])
            estrella.ibiv = int(lista[10])
            estrella.epav = float(lista[11])
            estrella.ep1 = float(lista[12])
            estrella.ep2 = float(lista[13])
            estrella.mp = int(lista[14])
            estrella.np = int(lista[15])
            estrella.nc = int(lista[16])
            estrella.spmid = lista[17]
            estrella.igalicat = int(lista[18])
            estrella.j = float(lista[19])
            estrella.h = float(lista[20])
            estrella.k = float(lista[21])
            estrella.save()

            if c == 5000:
                break
            c = c+1
            #break
        context['listo'] = "lista"
        return context
