from django.shortcuts import render, get_list_or_404
from bellafral.models import Simulations
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

            simulation.fralda_object.save()
            
            simulations_list.append(simulation)

        return render(request, 'index.html', {'simulations': simulations_list})
    
    except:
        return render(request, 'index.html', {'simulations': [], 'total_cost': 0})