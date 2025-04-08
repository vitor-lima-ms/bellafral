from django import forms
from bellafral.models import Bellafral
from stock.models import Stock

class BellafralForm(forms.ModelForm):
    class Meta:
        model = Bellafral
        fields = '__all__'

class BellafralSimulatorForm(forms.Form):
    fralda = forms.ModelChoiceField(queryset=Bellafral.objects.all())
    stock = forms.ModelChoiceField(queryset=Stock.objects.all())