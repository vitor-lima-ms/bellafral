from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from bellafral.models import Simulations, Bellafral
from bellafral.my_forms import BellafralEditForm
from base_dir.functions import get_total_cost

# Create your views here.

def index(request):
    try:
        simulations = get_list_or_404(Simulations)
        
        simulations_list = []
        for simulation in simulations:
            total_cost = get_total_cost(simulation.fralda_object, simulation.costs_object)
            simulation.fralda_object.total_cost = round(total_cost, 4)

            simulation.fralda_object.celulose_virgem_total_unit_cost = round(simulation.fralda_object.celulose_virgem * simulation.costs_object.celulose_virgem_price, 4)
            simulation.fralda_object.gel_total_unit_cost = round(simulation.fralda_object.gel * simulation.costs_object.gel_price, 4)
            simulation.fralda_object.tnt_filtrante_780_total_unit_cost = round(simulation.fralda_object.tnt_filtrante_780 * simulation.costs_object.tnt_filtrante_780_price, 4)
            simulation.fralda_object.fita_adesiva_tape_total_unit_cost = round(simulation.fralda_object.fita_adesiva_tape * simulation.costs_object.fita_adesiva_tape_price, 4)
            simulation.fralda_object.elastico_elastano_lycra_total_unit_cost = round(simulation.fralda_object.elastico_elastano_lycra * simulation.costs_object.elastico_elastano_lycra_price, 4)
            simulation.fralda_object.barreira_total_unit_cost = round(simulation.fralda_object.barreira * simulation.costs_object.barreira_price, 4)
            simulation.fralda_object.polietileno_filme_780_total_unit_cost = round(simulation.fralda_object.polietileno_filme_780 * simulation.costs_object.polietileno_filme_780_price, 4)
            simulation.fralda_object.hot_melt_const_total_unit_cost = round(simulation.fralda_object.hot_melt_const * simulation.costs_object.hot_melt_const_price, 4)

            simulation.fralda_object.custo_pacote = round((total_cost * simulation.fralda_object.qtd_p_pacote) + simulation.fralda_object.embalagem + simulation.fralda_object.saco_fardos, 4)
            simulation.fralda_object.custo_unitario_final = round(simulation.fralda_object.custo_pacote / simulation.fralda_object.qtd_p_pacote, 4)

            simulation.fralda_object.preco_venda = round((simulation.fralda_object.custo_pacote) / (1 - (simulation.fralda_object.comissao + simulation.fralda_object.impostos + simulation.fralda_object.frete + simulation.fralda_object.margem_contribuicao + simulation.fralda_object.st) / 100), 4)
            simulation.fralda_object.preco_venda_unitario = round(simulation.fralda_object.preco_venda / simulation.fralda_object.qtd_p_pacote, 4)

            simulation.fralda_object.preco_venda_st = round(simulation.fralda_object.preco_venda * (1 + simulation.fralda_object.st / 100), 4)
            simulation.fralda_object.preco_venda_st_unitario = round(simulation.fralda_object.preco_venda_st / simulation.fralda_object.qtd_p_pacote, 4)
            
            simulation.fralda_object.save()
            simulation.costs_object.save()
            simulation.save()
            
            simulations_list.append(simulation)
        
        return render(request, 'index.html', {'simulations': simulations_list})
    
    except:
        print('Entrou no except')
        return render(request, 'index.html', {'simulations': []})

def simulator_edit(request, id):
    simulation = get_object_or_404(Simulations, id=id)
    fralda = get_object_or_404(Bellafral, id=simulation.fralda_object.id)
    form = BellafralEditForm(instance=fralda)
    return render(request, 'simulator_edit.html', {'simulation': simulation, 'fralda': fralda, 'form': form})

def simulator_save(request, id):
    simulation = get_object_or_404(Simulations, id=id)
    fralda = get_object_or_404(Bellafral, id=simulation.fralda_object.id)
    form = BellafralEditForm(request.POST, instance=fralda)
    if form.is_valid():
        form.save()
    
    return redirect('core:index')
    