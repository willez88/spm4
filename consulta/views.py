from django.shortcuts import render

# Create your views here.

def parametros(request):
    return render(request, 'consulta.parametros.template.html')

def resultado_parametros(request):
    if request.method == "POST":
        print(request.POST['spmid_1'])
        print(request.POST['spmid_2'])

    return render(request, 'consulta.resultados.parametros.html')
