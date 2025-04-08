from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib import messages
from bellafral.my_forms import BellafralForm, BellafralSimulatorForm
from bellafral.models import Bellafral, Simulations
from base_dir.functions import get_total_cost
import csv

# Create your views here.

def bellafral_form(request):
    if request.method == 'POST':
        form = BellafralForm(request.POST)
        if form.is_valid():
            for value in form.cleaned_data.values():
                if type(value) == str:
                    continue
                elif value < 0:
                    messages.error(request, 'Valores não podem ser negativos')
                    return redirect('bellafral:bellafral_form')

            form.save()
            messages.success(request, 'Bellafral criada com sucesso')
            return redirect('bellafral:bellafral_list')
    else:
        form = BellafralForm()
    return render(request, 'bellafral_form.html', {'form': form})

def bellafral_list(request):
    bellafral = Bellafral.objects.all()
    return render(request, 'bellafral_list.html', {'bellafral': bellafral})

def bellafral_details(request, id):
    fralda = get_object_or_404(Bellafral, id=id)
    return render(request, 'bellafral_details.html', {'fralda': fralda})

def bellafral_delete(request, id):
    fralda = get_object_or_404(Bellafral, id=id)
    fralda.delete()
    return redirect('bellafral:bellafral_list')

def bellafral_pre_simulator(request):
    form = BellafralSimulatorForm()
    return render(request, 'bellafral_pre_simulator.html', {'form': form})

def bellafral_simulator(request):
    if request.method == 'POST':
        form = BellafralSimulatorForm(request.POST)
        
        if form.is_valid():
            fralda = form.cleaned_data['fralda']
            print(fralda)
            costs = form.cleaned_data['costs']
    else:
        form = BellafralSimulatorForm()

    total_cost = get_total_cost(fralda, costs)

    for key in total_cost.keys():
        total_cost[key] = float(total_cost[key])

    simulation = Simulations.objects.create(
        fralda={
                'celulose_virgem': float(fralda.celulose_virgem),
                'gel': float(fralda.gel),
                'tnt_filtrante_780': float(fralda.tnt_filtrante_780),
                'fita_adesiva_tape': float(fralda.fita_adesiva_tape),
                'elastico_elastano_lycra': float(fralda.elastico_elastano_lycra),
                'barreira': float(fralda.barreira),
                'polietileno_filme_780': float(fralda.polietileno_filme_780),
                'hot_melt_const': float(fralda.hot_melt_const),
            },
        fralda_object=fralda,
        costs={
                'celulose_virgem_price': float(costs.celulose_virgem_price),
                'gel_price': float(costs.gel_price),
                'tnt_filtrante_780_price': float(costs.tnt_filtrante_780_price),
                'fita_adesiva_tape_price': float(costs.fita_adesiva_tape_price),
                'elastico_elastano_lycra_price': float(costs.elastico_elastano_lycra_price),
                'barreira_price': float(costs.barreira_price),
                'polietileno_filme_780_price': float(costs.polietileno_filme_780_price),
                'hot_melt_const_price': float(costs.hot_melt_const_price),
            },
        costs_object=costs,
        simulation=total_cost,
        )
    simulation.save()

    return render(request, 'bellafral_simulator.html', {'costs': costs, 'fralda': fralda, 'total_cost': total_cost, 'simulation': simulation})

def download_simulation(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="simulation.csv"'

    csv_writer = csv.writer(response)

    simulation = Simulations.objects.last()

    csv_writer.writerow(
        [
            'Item',
            'Quantidade',
            'Custo unitário',
            'Custo total',
        ]
    )

    csv_writer.writerow(
        [
            'Celulose virgem (Kg)',
            simulation.fralda['celulose_virgem'],
            simulation.costs['celulose_virgem_price'],
            simulation.simulation['celulose_virgem'],
        ]
    )

    csv_writer.writerow(
        [
            'Gel (Kg)',
            simulation.fralda['gel'],
            simulation.costs['gel_price'],
            simulation.simulation['gel'],
        ]
    )

    csv_writer.writerow(
        [
            'TNT - Filtrante - 780mm (m2)',
            simulation.fralda['tnt_filtrante_780'],
            simulation.costs['tnt_filtrante_780_price'],
            simulation.simulation['tnt_filtrante_780'],
        ]
    )

    csv_writer.writerow(
        [
            'Fita adesiva - Tape (Kg)',
            simulation.fralda['fita_adesiva_tape'],
            simulation.costs['fita_adesiva_tape_price'],
            simulation.simulation['fita_adesiva_tape'],
        ]
    )

    csv_writer.writerow(
        [
            'Elástico - Elastano - Lycra (Kg)',
            simulation.fralda['elastico_elastano_lycra'],
            simulation.costs['elastico_elastano_lycra_price'],
            simulation.simulation['elastico_elastano_lycra'],
        ]
    )

    csv_writer.writerow(
        [
            'Barreira (m2)',
            simulation.fralda['barreira'],
            simulation.costs['barreira_price'],
            simulation.simulation['barreira'],
        ]
    )

    csv_writer.writerow(
        [
            'Polietileno - Filme - 780mm (Kg)',
            simulation.fralda['polietileno_filme_780'],
            simulation.costs['polietileno_filme_780_price'],
            simulation.simulation['polietileno_filme_780'],
        ]
    )

    csv_writer.writerow(
        [
            'Hot-Melt Construção (Kg)',
            simulation.fralda['hot_melt_const'],
            simulation.costs['hot_melt_const_price'],
            simulation.simulation['hot_melt_const'],
        ]
    )

    csv_writer.writerow(
        [
            'Custo total',
            simulation.simulation['total_cost'],
        ]
    )
    
    return response

def simulator_list(request):
    simulations = Simulations.objects.all()
    return render(request, 'simulator_list.html', {'simulations': simulations})

def simulator_details(request, id):
    simulation = get_object_or_404(Simulations, id=id)
    return render(request, 'simulator_details.html', {'costs': simulation.costs, 'fralda': simulation.fralda, 'total_cost': simulation.simulation, 'simulation': simulation})

def simulator_delete(request, id):
    simulation = get_object_or_404(Simulations, id=id)
    simulation.delete()
    return redirect('bellafral:simulator_list')
