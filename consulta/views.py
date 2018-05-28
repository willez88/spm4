from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .forms import ParametroForm, RectanguloForm
from .models import Estrella
import json
from django.http import HttpResponse
import csv

# Create your views here.

class ParametroView(FormView):
    template_name = 'consulta.parametro.template.html'
    form_class = ParametroForm
    #success_url = reverse_lazy('resultado')

    def form_valid(self, form):
        lista_and = []
        lista_or = []
        op_and = {}
        op_or = {}

        spmid_operador = form.cleaned_data['spmid_operador']
        spmid = form.cleaned_data['spmid']
        operador_logico_1 = form.cleaned_data['operador_logico_1']

        ra_operador = form.cleaned_data['ra_operador']
        ra = float(form.cleaned_data['ra'])
        #ra = float(ra)
        operador_logico_2 = form.cleaned_data['operador_logico_2']

        dec_operador = form.cleaned_data['dec_operador']
        dec = float(form.cleaned_data['dec'])
        #dec = float(dec)
        operador_logico_3 = form.cleaned_data['operador_logico_3']

        era_operador = form.cleaned_data['era_operador']
        era = float(form.cleaned_data['era'])
        #era = float(era)
        operador_logico_4 = form.cleaned_data['operador_logico_4']

        edec_operador = form.cleaned_data['edec_operador']
        edec = float(form.cleaned_data['edec'])
        #edec = float(edec)
        operador_logico_5 = form.cleaned_data['operador_logico_5']

        pma_operador = form.cleaned_data['pma_operador']
        pma = float(form.cleaned_data['pma'])
        operador_logico_6 = form.cleaned_data['operador_logico_6']

        pmd_operador = form.cleaned_data['pmd_operador']
        pmd = float(form.cleaned_data['pmd'])
        operador_logico_7 = form.cleaned_data['operador_logico_7']

        epma_operador = form.cleaned_data['epma_operador']
        epma = float(form.cleaned_data['epma'])
        operador_logico_8 = form.cleaned_data['operador_logico_8']

        epmd_operador = form.cleaned_data['epmd_operador']
        epmd = float(form.cleaned_data['epmd'])
        operador_logico_9 = form.cleaned_data['operador_logico_9']

        b_operador = form.cleaned_data['b_operador']
        b = float(form.cleaned_data['b'])
        operador_logico_10 = form.cleaned_data['operador_logico_10']

        v_operador = form.cleaned_data['v_operador']
        v = float(form.cleaned_data['v'])
        operador_logico_11 = form.cleaned_data['operador_logico_11']

        ibiv_operador = form.cleaned_data['ibiv_operador']
        ibiv = int(form.cleaned_data['ibiv'])
        operador_logico_12 = form.cleaned_data['operador_logico_12']

        epav_operador = form.cleaned_data['epav_operador']
        epav = float(form.cleaned_data['epav'])
        operador_logico_13 = form.cleaned_data['operador_logico_13']

        ep1_operador = form.cleaned_data['ep1_operador']
        ep1 = float(form.cleaned_data['ep1'])
        operador_logico_14 = form.cleaned_data['operador_logico_14']

        ep2_operador = form.cleaned_data['ep2_operador']
        ep2 = float(form.cleaned_data['ep2'])
        operador_logico_15 = form.cleaned_data['operador_logico_15']

        mp_operador = form.cleaned_data['mp_operador']
        mp = int(form.cleaned_data['mp'])
        operador_logico_16 = form.cleaned_data['operador_logico_16']

        np_operador = form.cleaned_data['np_operador']
        np = int(form.cleaned_data['np'])
        operador_logico_17 = form.cleaned_data['operador_logico_17']

        nc_operador = form.cleaned_data['nc_operador']
        nc = int(form.cleaned_data['nc'])
        operador_logico_18 = form.cleaned_data['operador_logico_18']

        igalicat_operador = form.cleaned_data['igalicat_operador']
        igalicat = int(form.cleaned_data['igalicat'])
        operador_logico_19 = form.cleaned_data['operador_logico_19']

        j_operador = form.cleaned_data['j_operador']
        j = float(form.cleaned_data['j'])
        operador_logico_20 = form.cleaned_data['operador_logico_20']

        h_operador = form.cleaned_data['h_operador']
        h = float(form.cleaned_data['h'])
        operador_logico_21 = form.cleaned_data['operador_logico_21']

        k_operador = form.cleaned_data['k_operador']
        k = float(form.cleaned_data['k'])

        if spmid_operador == '<':
            d1 = {'spmid':{'$lt':spmid}}
        elif spmid_operador == '<=':
            d1 = {'spmid':{'$lte':spmid}}
        elif spmid_operador == '>':
            d1 = {'spmid':{'$gt':spmid}}
        elif spmid_operador == '>=':
            d1 = {'spmid':{'$gte':spmid}}

        if ra_operador == '<':
            d2 = {'ra':{'$lt':ra}}
        elif ra_operador == '<=':
            d2 = {'ra':{'$lte':ra}}
        elif ra_operador == '>':
            d2 = {'ra':{'$gt':ra}}
        elif ra_operador == '>=':
            d2 = {'ra':{'$gte':ra}}

        if operador_logico_1 == 'and':
            lista_and.append(d1)
            lista_and.append(d2)
            #op1 = {'$and': lista_and}
        elif operador_logico_1 == 'or':
            lista_or.append(d1)
            lista_or.append(d2)
            #op1 = {'$or': lista_or}

        if dec_operador == '<':
            d3 = {'dec':{'$lt':dec}}
        elif dec_operador == '<=':
            d3 = {'dec':{'$lte':dec}}
        elif dec_operador == '>':
            d3 = {'dec':{'$gt':dec}}
        elif dec_operador == '>=':
            d3 = {'dec':{'$gte':dec}}

        if operador_logico_2 == 'and':
            lista_and.append(d2)
            lista_and.append(d3)
        elif operador_logico_2 == 'or':
            lista_or.append(d2)
            lista_or.append(d3)

        if era_operador == '<':
            d4 = {'era':{'$lt':era}}
        elif dec_operador == '<=':
            d4 = {'era':{'$lte':era}}
        elif era_operador == '>':
            d4 = {'era':{'$gt':era}}
        elif era_operador == '>=':
            d4 = {'era':{'$gte':era}}

        if operador_logico_3 == 'and':
            lista_and.append(d3)
            lista_and.append(d4)
        elif operador_logico_3 == 'or':
            lista_or.append(d3)
            lista_or.append(d4)

        if edec_operador == '<':
            d5 = {'edec':{'$lt':edec}}
        elif edec_operador == '<=':
            d5 = {'edec':{'$lte':edec}}
        elif edec_operador == '>':
            d5 = {'edec':{'$gt':edec}}
        elif edec_operador == '>=':
            d5 = {'edec':{'$gte':edec}}

        if operador_logico_4 == 'and':
            lista_and.append(d4)
            lista_and.append(d5)
        elif operador_logico_4 == 'or':
            lista_or.append(d4)
            lista_or.append(d5)

        if pma_operador == '<':
            d6 = {'pma':{'$lt':pma}}
        elif pma_operador == '<=':
            d6 = {'pma':{'$lte':pma}}
        elif pma_operador == '>':
            d6 = {'pma':{'$gt':pma}}
        elif pma_operador == '>=':
            d6 = {'pma':{'$gte':pma}}

        if operador_logico_5 == 'and':
            lista_and.append(d5)
            lista_and.append(d6)
        elif operador_logico_5 == 'or':
            lista_or.append(d5)
            lista_or.append(d6)

        if pmd_operador == '<':
            d7 = {'pmd':{'$lt':pmd}}
        elif pmd_operador == '<=':
            d7 = {'pmd':{'$lte':pmd}}
        elif pmd_operador == '>':
            d7 = {'pmd':{'$gt':pmd}}
        elif pmd_operador == '>=':
            d7 = {'pmd':{'$gte':pmd}}

        if operador_logico_6 == 'and':
            lista_and.append(d6)
            lista_and.append(d7)
        elif operador_logico_6 == 'or':
            lista_or.append(d6)
            lista_or.append(d7)

        if epma_operador == '<':
            d8 = {'epma':{'$lt':epma}}
        elif epma_operador == '<=':
            d8 = {'epma':{'$lte':epma}}
        elif epma_operador == '>':
            d8 = {'epma':{'$gt':epma}}
        elif epma_operador == '>=':
            d8 = {'epma':{'$gte':epma}}

        if operador_logico_7 == 'and':
            lista_and.append(d7)
            lista_and.append(d8)
        elif operador_logico_7 == 'or':
            lista_or.append(d7)
            lista_or.append(d8)

        if epmd_operador == '<':
            d9 = {'epmd':{'$lt':epmd}}
        elif epmd_operador == '<=':
            d9 = {'epmd':{'$lte':epmd}}
        elif epmd_operador == '>':
            d9 = {'epmd':{'$gt':epmd}}
        elif epmd_operador == '>=':
            d9 = {'epmd':{'$gte':epmd}}

        if operador_logico_8 == 'and':
            lista_and.append(d8)
            lista_and.append(d9)
        elif operador_logico_8 == 'or':
            lista_or.append(d8)
            lista_or.append(d9)

        if b_operador == '<':
            d10 = {'b':{'$lt':b}}
        elif b_operador == '<=':
            d10 = {'b':{'$lte':b}}
        elif b_operador == '>':
            d10 = {'b':{'$gt':b}}
        elif b_operador == '>=':
            d10 = {'b':{'$gte':b}}

        if operador_logico_9 == 'and':
            lista_and.append(d9)
            lista_and.append(d10)
        elif operador_logico_9 == 'or':
            lista_or.append(d9)
            lista_or.append(d10)

        if v_operador == '<':
            d11 = {'v':{'$lt':v}}
        elif v_operador == '<=':
            d11 = {'v':{'$lte':v}}
        elif v_operador == '>':
            d11 = {'v':{'$gt':v}}
        elif v_operador == '>=':
            d11 = {'v':{'$gte':v}}

        if operador_logico_10 == 'and':
            lista_and.append(d10)
            lista_and.append(d11)
        elif operador_logico_10 == 'or':
            lista_or.append(d10)
            lista_or.append(d11)

        if ibiv_operador == '<':
            d12 = {'ibiv':{'$lt':ibiv}}
        elif ibiv_operador == '<=':
            d12 = {'ibiv':{'$lte':ibiv}}
        elif ibiv_operador == '>':
            d12 = {'ibiv':{'$gt':ibiv}}
        elif ibiv_operador == '>=':
            d12 = {'ibiv':{'$gte':ibiv}}

        if operador_logico_11 == 'and':
            lista_and.append(d11)
            lista_and.append(d12)
        elif operador_logico_11 == 'or':
            lista_or.append(d11)
            lista_or.append(d12)

        if epav_operador == '<':
            d13 = {'epav':{'$lt':epav}}
        elif epav_operador == '<=':
            d13 = {'epav':{'$lte':epav}}
        elif epav_operador == '>':
            d13 = {'epav':{'$gt':epav}}
        elif epav_operador == '>=':
            d13 = {'epav':{'$gte':epav}}

        if operador_logico_12 == 'and':
            lista_and.append(d12)
            lista_and.append(d13)
        elif operador_logico_12 == 'or':
            lista_or.append(d12)
            lista_or.append(d13)

        if ep1_operador == '<':
            d14 = {'ep1':{'$lt':ep1}}
        elif ep1_operador == '<=':
            d14 = {'ep1':{'$lte':ep1}}
        elif ep1_operador == '>':
            d14 = {'ep1':{'$gt':ep1}}
        elif ep1_operador == '>=':
            d14 = {'ep1':{'$gte':ep1}}

        if operador_logico_13 == 'and':
            lista_and.append(d13)
            lista_and.append(d14)
        elif operador_logico_13 == 'or':
            lista_or.append(d13)
            lista_or.append(d14)

        if ep2_operador == '<':
            d15 = {'ep2':{'$lt':ep2}}
        elif ep2_operador == '<=':
            d15 = {'ep2':{'$lte':ep2}}
        elif ep2_operador == '>':
            d15 = {'ep2':{'$gt':ep2}}
        elif ep2_operador == '>=':
            d15 = {'ep2':{'$gte':ep2}}

        if operador_logico_14 == 'and':
            lista_and.append(d14)
            lista_and.append(d15)
        elif operador_logico_14 == 'or':
            lista_or.append(d14)
            lista_or.append(d15)

        if mp_operador == '<':
            d16 = {'mp':{'$lt':mp}}
        elif mp_operador == '<=':
            d16 = {'mp':{'$lte':mp}}
        elif mp_operador == '>':
            d16 = {'mp':{'$gt':mp}}
        elif mp_operador == '>=':
            d16 = {'mp':{'$gte':mp}}

        if operador_logico_15 == 'and':
            lista_and.append(d15)
            lista_and.append(d16)
        elif operador_logico_15 == 'or':
            lista_or.append(d15)
            lista_or.append(d16)

        if np_operador == '<':
            d17 = {'np':{'$lt':np}}
        elif np_operador == '<=':
            d17 = {'np':{'$lte':np}}
        elif np_operador == '>':
            d17 = {'np':{'$gt':np}}
        elif np_operador == '>=':
            d17 = {'np':{'$gte':np}}

        if operador_logico_16 == 'and':
            lista_and.append(d16)
            lista_and.append(d17)
        elif operador_logico_16 == 'or':
            lista_or.append(d16)
            lista_or.append(d17)

        if nc_operador == '<':
            d18 = {'nc':{'$lt':nc}}
        elif nc_operador == '<=':
            d18 = {'nc':{'$lte':nc}}
        elif nc_operador == '>':
            d18 = {'nc':{'$gt':nc}}
        elif nc_operador == '>=':
            d18 = {'nc':{'$gte':nc}}

        if operador_logico_17 == 'and':
            lista_and.append(d17)
            lista_and.append(d18)
        elif operador_logico_17 == 'or':
            lista_or.append(d17)
            lista_or.append(d18)

        if igalicat_operador == '<':
            d19 = {'igalicat':{'$lt':igalicat}}
        elif igalicat_operador == '<=':
            d19 = {'igalicat':{'$lte':igalicat}}
        elif igalicat_operador == '>':
            d19 = {'igalicat':{'$gt':igalicat}}
        elif igalicat_operador == '>=':
            d19 = {'igalicat':{'$gte':igalicat}}

        if operador_logico_18 == 'and':
            lista_and.append(d18)
            lista_and.append(d19)
        elif operador_logico_18 == 'or':
            lista_or.append(d18)
            lista_or.append(d19)

        if j_operador == '<':
            d20 = {'j':{'$lt':j}}
        elif j_operador == '<=':
            d20 = {'j':{'$lte':j}}
        elif j_operador == '>':
            d20 = {'j':{'$gt':j}}
        elif j_operador == '>=':
            d20 = {'j':{'$gte':j}}

        if operador_logico_19 == 'and':
            lista_and.append(d19)
            lista_and.append(d20)
        elif operador_logico_19 == 'or':
            lista_or.append(d19)
            lista_or.append(d20)

        if h_operador == '<':
            d21 = {'h':{'$lt':h}}
        elif h_operador == '<=':
            d21 = {'h':{'$lte':h}}
        elif h_operador == '>':
            d21 = {'h':{'$gt':h}}
        elif h_operador == '>=':
            d21 = {'h':{'$gte':h}}

        if operador_logico_20 == 'and':
            lista_and.append(d20)
            lista_and.append(d21)
        elif operador_logico_20 == 'or':
            lista_or.append(d20)
            lista_or.append(d21)

        if k_operador == '<':
            d22 = {'k':{'$lt':k}}
        elif k_operador == '<=':
            d22 = {'k':{'$lte':k}}
        elif k_operador == '>':
            d22 = {'k':{'$gt':k}}
        elif k_operador == '>=':
            d22 = {'k':{'$gte':k}}

        if operador_logico_21 == 'and':
            lista_and.append(d21)
            lista_and.append(d22)
        elif operador_logico_21 == 'or':
            lista_or.append(d21)
            lista_or.append(d22)

        total = {}
        #print(lista_and)
        #print(lista_or)
        op1 = {'$and': lista_and}
        op2 = {'$or': lista_or}
        print(op1)
        print(op2)
        if len(lista_or)==0:
            total = op1
            #print('and')
        elif len(lista_and)==0:
            total = op2
            #print('or')
        elif len(lista_and)>0 and len(lista_or)>0:
            op10.update(op2)
            total = op1
            #print('hola')

        estrella = Estrella.objects.filter(
            __raw__= total
        )
        print(estrella.count())

        """temp = []
        c = 0
        for es in estrella:
            lista = []
            lista.append(es.spmid)
            lista.append(es.ra)
            lista.append(es.dec)
            lista.append(es.era)
            temp.append(lista)
            if c == 10:
                break
            c = c + 1
        d = {'data': temp}
        print(d)"""
        if form.cleaned_data['opcion'] == '1':
            return render(self.request, 'consulta.parametro.resultado.html', {'spm4': estrella.limit(5000)})
        elif form.cleaned_data['opcion'] == '2':
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="resultado.csv"'
            writer = csv.writer(response,delimiter=';')
            writer.writerow(['spmid', 'ra', 'dec', 'era','edec','pma','pmd','epma','epmd','b','v','ibiv','epav','ep1','ep2','mp','np','nc','igalicat','j','h','k'])
            for es in estrella:
                writer.writerow([es.spmid, es.ra, es.dec, es.era,es.edec,es.pma,es.pmd,es.epma,es.epmd,es.b,es.v,es.ibiv,es.epav,es.ep1,es.ep2,es.mp,es.np,es.nc,es.igalicat,es.j,es.h,es.k])
            return response
        elif form.cleaned_data['opcion'] == '3':
            lista = []
            for es in estrella:
                #lista = []
                lista.append({'spmid':es.spmid,'ra':es.ra,'era':es.era,'edec':es.edec,'pma':es.pma,'pmd':es.pmd,'epma':es.epma,'epmd':es.epmd,'b':es.b,'v':es.v,'ibiv':es.ibiv,
                    'epav':es.epav,'ep1':es.ep1,'ep2':es.ep2,'mp':es.mp,'np':es.np,'nc':es.nc,'igalicat':es.igalicat,'j':es.j,'h':es.h,'k':es.k
                })
            response = HttpResponse(json.dumps(lista), content_type='application/force-download')
            response['Content-Disposition'] = 'attachment; filename="resultado.json"'
            return response
            #return HttpResponse(json.dumps(lista), content_type='application/force-download')

    def form_invalid(self, form):
        print(form.errors)
        return super(ParametroView, self).form_invalid(form)

class CargarDatosView(TemplateView):
    template_name = 'consulta.cargar.datos.html'
    def get_context_data(self, **kwargs):
        context = super(CargarDatosView, self).get_context_data(**kwargs)
        cadena = ''
        cadena2 = ''
        c = 0
        archivo = open('/home/william/MongoDB-Proyecto/Catalogo-SPM4/rs.asc', 'r')
        for linea in archivo:
            lista = linea.split(' ')
            if len(lista) == 21:
                cadena = cadena + lista[14][len(lista[14])-2]
                cadena = cadena + lista[14][len(lista[14])-1]
                for i in range(0, len(lista[14])-2):
                    cadena2 = cadena2 + lista[14][i]
                #print(lista)
                #print(cadena)
                #print(cadena2)
                #break
                estrella = Estrella()
                estrella.ra = float(lista[0])
                estrella.dec = float(lista[1])
                estrella.era = float(lista[2])
                estrella.edec = float(lista[3])
                estrella.pma = float(lista[4])
                estrella.pmd = float(lista[5])
                estrella.epma = float(lista[6])
                estrella.epmd = float(lista[7])
                estrella.b = float(lista[8])
                estrella.v = float(lista[9])
                estrella.ibiv = int(lista[10])
                estrella.epav = float(lista[11])
                estrella.ep1 = float(lista[12])
                estrella.ep2 = float(lista[13])
                estrella.mp = int(cadena2)
                estrella.np = int(cadena)
                estrella.nc = int(lista[16])
                estrella.spmid = lista[17]
                estrella.igalicat = int(lista[18])
                estrella.j = float(lista[19])
                estrella.h = float(lista[20])
                estrella.k = float(lista[21])
                estrella.save()

            elif len(lista) == 22:
                estrella = Estrella()
                estrella.ra = float(lista[0])
                estrella.dec = float(lista[1])
                estrella.era = float(lista[2])
                estrella.edec = float(lista[3])
                estrella.pma = float(lista[4])
                estrella.pmd = float(lista[5])
                estrella.epma = float(lista[6])
                estrella.epmd = float(lista[7])
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

            """if c == 100000:
                break
            c = c+1"""
            #break
        context['listo'] = "Datos Cargados"
        return context

def datos_json(request):
    spm4 = request.POST.get('spm4', None)
    estrella = Estrella.objects.all();
    print(estrella.count())
    c = 0
    lista2 = []
    for es in estrella:
        lista = []
        lista.append(es.spmid)
        lista.append(es.ra)
        lista.append(es.dec)
        lista.append(es.era)
        lista.append(es.edec)
        lista.append(es.pma)
        lista.append(es.pmd)
        lista.append(es.epma)
        lista.append(es.epmd)
        lista.append(es.b)
        lista.append(es.v)
        lista.append(es.ibiv)
        lista.append(es.epav)
        lista.append(es.ep1)
        lista.append(es.ep2)
        lista.append(es.mp)
        lista.append(es.np)
        lista.append(es.nc)
        lista.append(es.igalicat)
        lista.append(es.j)
        lista.append(es.h)
        lista.append(es.k)
        lista2.append(lista)
        #if c == 10:
        #    break
        #c = c + 1
    return HttpResponse(json.dumps({'draw': 1,'recordsTotal': estrella.count(),'recordsFiltered': estrella.count(),'data': lista2}))

class RectanguloView(FormView):
    template_name = 'consulta.rectangulo.template.html'
    form_class = RectanguloForm
