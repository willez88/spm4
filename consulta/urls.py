from django.conf.urls import url, include
from . import views

urlpatterns = [

    url(r'^parametros/$', views.parametros, name='parametros'),
    url(r'^resultado-parametros/$', views.resultado_parametros, name='resultado_parametros'),
    #url(r'^registro$', EncuestadorCreate.as_view(), name='encuestador_registro'),
    #url(r'^editar/(?P<pk>\d+)$', EncuestadorUpdate.as_view(), name='encuestador_editar'),
    #url(r'^borrar/(?P<pk>\d+)$', EncuestadorDelete.as_view(), name='encuestador_borrar'),
    #url(r'^vivienda/', include('encuestador.vivienda.urls')),
]
