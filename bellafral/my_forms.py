from django import forms
from bellafral.models import Bellafral, Simulations
from costs.models import Costs

class BellafralForm(forms.ModelForm):
    class Meta:
        model = Bellafral
        fields = '__all__'

class BellafralSimulatorForm(forms.Form):
    fralda = forms.ModelChoiceField(queryset=Bellafral.objects.all())
    costs = forms.ModelChoiceField(queryset=Costs.objects.all())

class BellafralEditForm(forms.ModelForm):
    class Meta:
        model = Bellafral
        fields = [
            'celulose_virgem',
            'gel',
            'tnt_filtrante_780',
            'fita_adesiva_tape',
            'elastico_elastano_lycra',
            'barreira',
            'polietileno_filme_780',
            'hot_melt_const',
            'qtd_p_pacote',
            'embalagem',
            'saco_fardos',
            'comissao',
            'impostos',
            'frete',
            'margem_contribuicao',
            'st',
        ]


class SimulationEditForm(forms.ModelForm):
    class Meta:
        model = Simulations
        fields = '__all__'