from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from costs.my_forms import CostsForm, CostsBaseEditForm
from costs.models import Costs

# Create your views here.

def costs_base(request):
    cost = Costs.objects.get(identificador='Base')
    return render(request, 'costs_base.html', {'cost': cost})

def costs_base_edit(request, id):
    cost = get_object_or_404(Costs, id=id)
    form = CostsBaseEditForm(instance=cost)
    return render(request, 'costs_base_edit.html', {'form': form, 'cost': cost})

def costs_base_save(request, id):
    cost = get_object_or_404(Costs, id=id)
    form = CostsBaseEditForm(request.POST, instance=cost)
    if form.is_valid():
        form.save()
        return redirect('costs:costs_base')

def costs_form(request):
    if request.method == 'POST':
        form = CostsForm(request.POST)
        if form.is_valid():
            for value in form.cleaned_data.values():
                if type(value) == str or value == None:
                    continue
                elif value < 0:
                    messages.error(request, 'Valores não podem ser negativos')
                    return redirect('costs:costs_form')
            
            form.save()
            messages.success(request, 'Custos criados com sucesso')
            return redirect('costs:costs_list')
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
