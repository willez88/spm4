from django.conf.urls import url, include
from .views import ParametroView, CargarDatosView

urlpatterns = [
    url(r'^parametro/$', ParametroView.as_view(), name='parametro'),
    url(r'^cargar-datos/$', CargarDatosView.as_view(), name='cargar_datos'),
    #url(r'^datos-json/?$', datos_json, name='datos_json')
]
