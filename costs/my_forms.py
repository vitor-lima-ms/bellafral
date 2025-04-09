from django import forms
from costs.models import Costs

class CostsForm(forms.ModelForm):
    class Meta:
        model = Costs
        fields = '__all__'

class CostsBaseEditForm(forms.ModelForm):
    class Meta:
        model = Costs
        fields = '__all__'