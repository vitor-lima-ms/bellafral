from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from costs.my_forms import CostsForm
from costs.models import Costs

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

def costs_list(request):
    costs = Costs.objects.all()
    return render(request, 'costs_list.html', {'costs': costs})

def costs_details(request, id):
    cost = get_object_or_404(Costs, id=id)
    return render(request, 'costs_details.html', {'cost': cost})

def costs_delete(request, id):
    cost = get_object_or_404(Costs, id=id)
    cost.delete()
    return redirect('costs:costs_list')
