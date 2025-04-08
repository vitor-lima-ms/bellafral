from django.shortcuts import render, redirect
from django.contrib import messages
from stock.my_forms import StockForm
# Create your views here.

def stock_form(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Custos criados com sucesso')
            return redirect('core:index')
    else:
        form = StockForm()
    return render(request, 'stock_form.html', {'form': form})