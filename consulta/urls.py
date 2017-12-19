from django.conf.urls import url, include
from . import views
from .views import ParametroView, ResultadoView, DatosPruebaView

urlpatterns = [

    url(r'^parametros/$', views.parametros, name='parametros'),
    url(r'^resultado-parametros/$', views.resultado_parametros, name='resultado_parametros'),
    url(r'^parametros2/$', ParametroView.as_view(), name='parametros2'),
    url(r'^resultado/$', ResultadoView.as_view(), name='resultado'),
    url(r'^datos-prueba/$', DatosPruebaView.as_view(), name='datos_prueba'),
]
