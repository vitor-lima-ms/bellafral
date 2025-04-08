from django import forms
from stock.models import Stock

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'