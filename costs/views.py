from django.shortcuts import render, redirect
from django.contrib import messages
from costs.my_forms import CostsForm
# Create your views here.

def costs_form(request):
    if request.method == 'POST':
        form = CostsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Custos criados com sucesso')
            return redirect('core:index')
    else:
        form = CostsForm()
    return render(request, 'costs_form.html', {'form': form})