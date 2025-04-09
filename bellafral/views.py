from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib import messages
from bellafral.my_forms import BellafralForm, BellafralSimulatorForm, BellafralEditForm
from bellafral.models import Bellafral, Simulations
from base_dir.functions import get_total_cost
import csv

# Create your views here.

def bellafral_form(request):
    if request.method == 'POST':
        form = BellafralForm(request.POST)
        if form.is_valid():
            for value in form.cleaned_data.values():
                if type(value) == str or value == None:
                    continue
                elif value < 0:
                    messages.error(request, 'Valores não podem ser negativos')
                    return redirect('bellafral:bellafral_form')

            form.save()
            messages.success(request, 'Fralda criada com sucesso')
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

def bellafral_edit(request, id):
    fralda = get_object_or_404(Bellafral, id=id)
    form = BellafralEditForm(instance=fralda)
    return render(request, 'bellafral_edit.html', {'form': form, 'fralda': fralda})

def bellafral_edit_save(request, id):
    fralda = get_object_or_404(Bellafral, id=id)
    form = BellafralEditForm(request.POST, instance=fralda)
    if form.is_valid():
        form.save()
        return redirect('bellafral:bellafral_details', id=id)

def bellafral_pre_simulator(request):
    form = BellafralSimulatorForm()
    return render(request, 'bellafral_pre_simulator.html', {'form': form})

def bellafral_simulator(request):
    if request.method == 'POST':
            form = BellafralSimulatorForm(request.POST)
                        
            if form.is_valid():
                fralda = form.cleaned_data['fralda']
                costs = form.cleaned_data['costs']
    else:
        form = BellafralSimulatorForm()
        return render(request, 'bellafral_pre_simulator.html', {'form': form})

    total_cost = get_total_cost(fralda, costs)

    simulation = Simulations.objects.create(
        fralda_object=fralda,
        costs_object=costs,
        )
    
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

    simulation.save()

    
    return render(request, 'bellafral_simulator.html', {'total_cost': total_cost, 'simulation': simulation})

def download_simulation(request, id):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="simulation.csv"'

    csv_writer = csv.writer(response)

    simulation = get_object_or_404(Simulations, id=id)
    total_cost = get_total_cost(simulation.fralda_object, simulation.costs_object)

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
            simulation.fralda_object.celulose_virgem,
            simulation.costs_object.celulose_virgem_price,
            round(simulation.fralda_object.celulose_virgem * simulation.costs_object.celulose_virgem_price, 4),
        ]
    )

    csv_writer.writerow(
        [
            'Gel (Kg)',
            simulation.fralda_object.gel,
            simulation.costs_object.gel_price,
            round(simulation.fralda_object.gel * simulation.costs_object.gel_price, 4),
        ]
    )

    csv_writer.writerow(
        [
            'TNT - Filtrante - 780mm (m2)',
            simulation.fralda_object.tnt_filtrante_780,
            simulation.costs_object.tnt_filtrante_780_price,
            round(simulation.fralda_object.tnt_filtrante_780 * simulation.costs_object.tnt_filtrante_780_price, 4),
        ]
    )

    csv_writer.writerow(
        [
            'Fita adesiva - Tape (Kg)',
            simulation.fralda_object.fita_adesiva_tape,
            simulation.costs_object.fita_adesiva_tape_price,
            round(simulation.fralda_object.fita_adesiva_tape * simulation.costs_object.fita_adesiva_tape_price, 4),
        ]
    )

    csv_writer.writerow(
        [
            'Elástico - Elastano - Lycra (Kg)',
            simulation.fralda_object.elastico_elastano_lycra,
            simulation.costs_object.elastico_elastano_lycra_price,
            round(simulation.fralda_object.elastico_elastano_lycra * simulation.costs_object.elastico_elastano_lycra_price, 4),
        ]
    )

    csv_writer.writerow(
        [
            'Barreira (m2)',
            simulation.fralda_object.barreira,
            simulation.costs_object.barreira_price,
            round(simulation.fralda_object.barreira * simulation.costs_object.barreira_price, 4),
        ]
    )

    csv_writer.writerow(
        [
            'Polietileno - Filme - 780mm (Kg)',
            simulation.fralda_object.polietileno_filme_780,
            simulation.costs_object.polietileno_filme_780_price,
            round(simulation.fralda_object.polietileno_filme_780 * simulation.costs_object.polietileno_filme_780_price, 4),
        ]
    )

    csv_writer.writerow(
        [
            'Hot-Melt Construção (Kg)',
            simulation.fralda_object.hot_melt_const,
            simulation.costs_object.hot_melt_const_price,
            round(simulation.fralda_object.hot_melt_const * simulation.costs_object.hot_melt_const_price, 4),
        ]
    )

    csv_writer.writerow(
        [
            'Custo total',
            total_cost,
        ]
    )

    csv_writer.writerow(
        [
            'Quantidade de peças por pacote',
            simulation.fralda_object.qtd_p_pacote,
        ]
    )

    csv_writer.writerow(
        [
            'Embalagem (R$)',
            simulation.fralda_object.embalagem,
        ]
    )

    csv_writer.writerow(
        [
            'Saco para fardos (R$)',
            simulation.fralda_object.saco_fardos,
        ]
    )

    csv_writer.writerow(
        [
            'Custo do pacote (R$)',
            simulation.fralda_object.custo_pacote,
        ]
    )

    csv_writer.writerow(
        [
            'Custo unitário final (R$)',
            simulation.fralda_object.custo_unitario_final,
        ]
    )

    csv_writer.writerow(
        [
            'Comissão (%)',
            simulation.fralda_object.comissao,
        ]
    )

    csv_writer.writerow(
        [
            'Impostos (%)',
            simulation.fralda_object.impostos,
        ]
    )

    csv_writer.writerow(
        [
            'Frete (%)',
            simulation.fralda_object.frete,
        ]
    )

    csv_writer.writerow(
        [
            'Margem de contribuição (%)',
            simulation.fralda_object.margem_contribuicao,
        ]
    )

    csv_writer.writerow(
        [
            'ST (%)',
            simulation.fralda_object.st,
        ]
    )

    csv_writer.writerow(
        [
            'Preço de venda (R$)',
            simulation.fralda_object.preco_venda,
        ]
    )

    csv_writer.writerow(
        [
            'Preço de venda unitário (R$)',
            simulation.fralda_object.preco_venda_unitario,
        ]
    )

    csv_writer.writerow(
        [
            'Preço de venda com ST (R$)',
            simulation.fralda_object.preco_venda_st,
        ]
    )

    csv_writer.writerow(
        [
            'Preço de venda unitário com ST (R$)',
            simulation.fralda_object.preco_venda_st_unitario,
        ]
    )

    return response

def simulator_list(request):
    simulations = Simulations.objects.all()
    return render(request, 'simulator_list.html', {'simulations': simulations})

def simulator_details(request, id):
    simulation = get_object_or_404(Simulations, id=id)
    total_cost = get_total_cost(simulation.fralda_object, simulation.costs_object)

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

    return render(request, 'simulator_details.html', {'simulation': simulation, 'total_cost': total_cost})

def simulator_delete(request, id):
    simulation = get_object_or_404(Simulations, id=id)
    simulation.delete()
    return redirect('bellafral:simulator_list')
