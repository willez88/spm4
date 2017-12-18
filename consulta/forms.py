from django import forms
from django.utils.translation import ugettext_lazy as _
from base.constant import OPERADOR_UNO, OPERADOR_DOS

class ParametroForm(forms.Form):

    spmid_operador = forms.ChoiceField(
        label=_("SPMID Operador"),
        choices= OPERADOR_UNO,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    spmid = forms.CharField(
        label=_("SPMID"),
        max_length=100,
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique el valor spmid"),
            }
        ), required = False
    )

    spmid_ra = forms.ChoiceField(
        label=_("SPMID y RA"),
        choices= OPERADOR_DOS,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )
