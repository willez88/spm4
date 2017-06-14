from django.conf.urls import url, include
from .views import parametros

urlpatterns = [

    url(r'^parametros/$', parametros, name='parametros'),
    #url(r'^(?P<pk>\d+)$', CourseDetail.as_view(), name='encuestador_detail'),
    #url(r'^registro$', EncuestadorCreate.as_view(), name='encuestador_registro'),
    #url(r'^editar/(?P<pk>\d+)$', EncuestadorUpdate.as_view(), name='encuestador_editar'),
    #url(r'^borrar/(?P<pk>\d+)$', EncuestadorDelete.as_view(), name='encuestador_borrar'),
    #url(r'^vivienda/', include('encuestador.vivienda.urls')),
]
