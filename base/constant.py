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

## Mensaje de error para peticiones AJAX
MSG_NOT_AJAX = _("No se puede procesar la petición. "
                 "Verifique que posea las opciones javascript habilitadas e intente nuevamente.")
