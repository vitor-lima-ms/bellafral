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

def bellafral_pre_simulator(request):
    form = BellafralSimulatorForm()
    return render(request, 'bellafral_pre_simulator.html', {'form': form})

def bellafral_simulator(request):
    if request.method == 'POST':
        form = BellafralSimulatorForm(request.POST)
        
        if form.is_valid():
            fralda = form.cleaned_data['fralda']
            print(fralda)
            stock = form.cleaned_data['stock']
    else:
        form = BellafralSimulatorForm()

    costs = get_total_cost(fralda, stock)

    for key in costs.keys():
        costs[key] = float(costs[key])

    simulation = Simulations.objects.create(
        fralda={
            fralda.nome: {
                'celulose_virgem': float(fralda.celulose_virgem),
                'gel': float(fralda.gel),
                'tnt_filtrante_780': float(fralda.tnt_filtrante_780),
                'fita_adesiva_tape': float(fralda.fita_adesiva_tape),
                'elastico_elastano_lycra': float(fralda.elastico_elastano_lycra),
                'barreira': float(fralda.barreira),
                'polietileno_filme_780': float(fralda.polietileno_filme_780),
                'hot_melt_const': float(fralda.hot_melt_const),
            }
        },
        stock={
            stock.nome: {
                'celulose_virgem_price': float(stock.celulose_virgem_price),
                'gel_price': float(stock.gel_price),
                'tnt_filtrante_780_price': float(stock.tnt_filtrante_780_price),
                'fita_adesiva_tape_price': float(stock.fita_adesiva_tape_price),
                'elastico_elastano_lycra_price': float(stock.elastico_elastano_lycra_price),
                'barreira_price': float(stock.barreira_price),
                'polietileno_filme_780_price': float(stock.polietileno_filme_780_price),
                'hot_melt_const_price': float(stock.hot_melt_const_price),
            }
        },
        simulation=costs,
    )
    simulation.save()

    return render(request, 'bellafral_simulator.html', {'costs': costs, 'fralda': fralda, 'stock': stock, 'simulation': simulation})

def download_simulation(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="simulation.csv"'

    csv_writer = csv.writer(response)

    simulation = Simulations.objects.last()

    csv_writer.writerow(
        [
            simulation.fralda,
            simulation.stock,
            simulation.simulation,
        ]
    )

    return response