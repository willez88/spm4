from django.conf.urls import url, include
from . import views

urlpatterns = [

    url(r'^parametros/$', views.parametros, name='parametros'),
    #url(r'^(?P<pk>\d+)$', CourseDetail.as_view(), name='encuestador_detail'),
    #url(r'^registro$', EncuestadorCreate.as_view(), name='encuestador_registro'),
    #url(r'^editar/(?P<pk>\d+)$', EncuestadorUpdate.as_view(), name='encuestador_editar'),
    #url(r'^borrar/(?P<pk>\d+)$', EncuestadorDelete.as_view(), name='encuestador_borrar'),
    #url(r'^vivienda/', include('encuestador.vivienda.urls')),
]
