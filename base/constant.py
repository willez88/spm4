from django.utils.translation import ugettext_lazy as _

## Operador de comparación simple
OPERADOR_UNO = (
    ("<",_("<")),
    ("<=",_("<=")),
    (">",_(">")),
    (">=",_(">=")),
    ("=",_("=")),
)

## Operador de comparación compuesta
OPERADOR_DOS = (
    ("and",_("&&")),
    ("or",_("||")),
)

## Opciones de visualización
OPCION = (
    ('1',_('HTML')),
    ('2',_('CSV')),
    ('3',_('JSON')),
)

## Mensaje de error para peticiones AJAX
MSG_NOT_AJAX = _("No se puede procesar la petición. "
                 "Verifique que posea las opciones javascript habilitadas e intente nuevamente.")
