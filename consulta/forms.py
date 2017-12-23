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

    operador_logico_1 = forms.ChoiceField(
        label=_("Operador Lógico 1"),
        choices= OPERADOR_DOS,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    ra_operador = forms.ChoiceField(
        choices= OPERADOR_UNO,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    ra = forms.CharField(
        label=_("RA"),
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique el valor RA"), 'step': 'any',
            }
        ), required = False
    )

    operador_logico_2 = forms.ChoiceField(
        choices= OPERADOR_DOS,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    dec_operador = forms.ChoiceField(
        choices= OPERADOR_UNO,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    dec = forms.CharField(
        label=_("DEC"),
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique el valor DEC"), 'step': 'any',
            }
        ), required = False
    )

    operador_logico_3 = forms.ChoiceField(
        choices= OPERADOR_DOS,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    era_operador = forms.ChoiceField(
        choices= OPERADOR_UNO,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    era = forms.CharField(
        label=_("ERA"),
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique el valor ERA"), 'step': 'any',
            }
        ), required = False
    )

    operador_logico_4 = forms.ChoiceField(
        choices= OPERADOR_DOS,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    edec_operador = forms.ChoiceField(
        choices= OPERADOR_UNO,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    edec = forms.CharField(
        label=_("EDEC"),
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique el valor EDEC"), 'step': 'any',
            }
        ), required = False
    )

    operador_logico_5 = forms.ChoiceField(
        choices= OPERADOR_DOS,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    pma_operador = forms.ChoiceField(
        choices= OPERADOR_UNO,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    pma = forms.CharField(
        label=_("PMA"),
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique el valor PMA"), 'step': 'any',
            }
        ), required = False
    )

    operador_logico_6 = forms.ChoiceField(
        choices= OPERADOR_DOS,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    pmd_operador = forms.ChoiceField(
        choices= OPERADOR_UNO,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    pmd = forms.CharField(
        label=_("PMD"),
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique el valor PMD"), 'step': 'any',
            }
        ), required = False
    )

    operador_logico_7 = forms.ChoiceField(
        choices= OPERADOR_DOS,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    epma_operador = forms.ChoiceField(
        choices= OPERADOR_UNO,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    epma = forms.CharField(
        label=_("EPMA"),
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique el valor EPMA"), 'step': 'any',
            }
        ), required = False
    )

    operador_logico_8 = forms.ChoiceField(
        choices= OPERADOR_DOS,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    epmd_operador = forms.ChoiceField(
        choices= OPERADOR_UNO,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    epmd = forms.CharField(
        label=_("EPMD"),
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique el valor EPMD"), 'step': 'any',
            }
        ), required = False
    )

    operador_logico_9 = forms.ChoiceField(
        choices= OPERADOR_DOS,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    b_operador = forms.ChoiceField(
        choices= OPERADOR_UNO,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    b = forms.CharField(
        label=_("B"),
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique el valor B"), 'step': 'any',
            }
        ), required = False
    )

    operador_logico_10 = forms.ChoiceField(
        choices= OPERADOR_DOS,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    v_operador = forms.ChoiceField(
        choices= OPERADOR_UNO,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    v = forms.CharField(
        label=_("V"),
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique el valor V"), 'step': 'any',
            }
        ), required = False
    )

    operador_logico_11 = forms.ChoiceField(
        choices= OPERADOR_DOS,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    ibiv_operador = forms.ChoiceField(
        choices= OPERADOR_UNO,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    ibiv = forms.CharField(
        label=_("IBIV"),
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique el valor IBIV"),
            }
        ), required = False
    )

    operador_logico_12 = forms.ChoiceField(
        choices= OPERADOR_DOS,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    epav_operador = forms.ChoiceField(
        choices= OPERADOR_UNO,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    epav = forms.CharField(
        label=_("EPAV"),
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique el valor EPAV"), 'step': 'any',
            }
        ), required = False
    )

    operador_logico_13 = forms.ChoiceField(
        choices= OPERADOR_DOS,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    ep1_operador = forms.ChoiceField(
        choices= OPERADOR_UNO,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    ep1 = forms.CharField(
        label=_("EP1"),
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique el valor EP1"), 'step': 'any',
            }
        ), required = False
    )

    operador_logico_14 = forms.ChoiceField(
        choices= OPERADOR_DOS,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    ep2_operador = forms.ChoiceField(
        choices= OPERADOR_UNO,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    ep2 = forms.CharField(
        label=_("EP2"),
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique el valor EP2"), 'step': 'any',
            }
        ), required = False
    )

    operador_logico_15 = forms.ChoiceField(
        choices= OPERADOR_DOS,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    mp_operador = forms.ChoiceField(
        choices= OPERADOR_UNO,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    mp = forms.CharField(
        label=_("MP"),
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique el valor MP"),
            }
        ), required = False
    )

    operador_logico_16 = forms.ChoiceField(
        choices= OPERADOR_DOS,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    np_operador = forms.ChoiceField(
        choices= OPERADOR_UNO,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    np = forms.CharField(
        label=_("NP"),
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique el valor NP"),
            }
        ), required = False
    )

    operador_logico_17 = forms.ChoiceField(
        choices= OPERADOR_DOS,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    nc_operador = forms.ChoiceField(
        choices= OPERADOR_UNO,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    nc = forms.CharField(
        label=_("NC"),
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique el valor NC"),
            }
        ), required = False
    )

    operador_logico_18 = forms.ChoiceField(
        choices= OPERADOR_DOS,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    igalicat_operador = forms.ChoiceField(
        choices= OPERADOR_UNO,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    igalicat = forms.CharField(
        label=_("IGALICAT"),
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique el valor IGALICAT"),
            }
        ), required = False
    )

    operador_logico_19 = forms.ChoiceField(
        choices= OPERADOR_DOS,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    j_operador = forms.ChoiceField(
        choices= OPERADOR_UNO,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"), 'step': 'any',
            }
        ), required= False
    )

    j = forms.CharField(
        label=_("J"),
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique el valor J"),
            }
        ), required = False
    )

    operador_logico_20 = forms.ChoiceField(
        choices= OPERADOR_DOS,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    h_operador = forms.ChoiceField(
        choices= OPERADOR_UNO,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    h = forms.CharField(
        label=_("H"),
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique el valor H"), 'step': 'any',
            }
        ), required = False
    )

    operador_logico_21 = forms.ChoiceField(
        choices= OPERADOR_DOS,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    k_operador = forms.ChoiceField(
        choices= OPERADOR_UNO,
        widget=forms.Select(
            attrs={
                'class': 'form-control select2', 'data-toggle': 'tooltip', 'style':'width:50px;',
                'title': _("Seleccione el Operador"),
            }
        ), required= False
    )

    k = forms.CharField(
        label=_("K"),
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip', 'style':'width:250px;',
                'title': _("Indique el valor K"), 'step': 'any',
            }
        ), required = False
    )
