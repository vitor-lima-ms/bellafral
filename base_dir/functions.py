def get_total_cost(fralda, cost):
    costs = {
        'celulose_virgem': round(fralda.celulose_virgem * cost.celulose_virgem_price, 4),
        'gel': round(fralda.gel * cost.gel_price, 4),
        'tnt_filtrante_780': round(fralda.tnt_filtrante_780 * cost.tnt_filtrante_780_price, 4),
        'fita_adesiva_tape': round(fralda.fita_adesiva_tape * cost.fita_adesiva_tape_price, 4),
        'elastico_elastano_lycra': round(fralda.elastico_elastano_lycra * cost.elastico_elastano_lycra_price, 4),
        'barreira': round(fralda.barreira * cost.barreira_price, 4),
        'polietileno_filme_780': round(fralda.polietileno_filme_780 * cost.polietileno_filme_780_price, 4),
        'hot_melt_const': round(fralda.hot_melt_const * cost.hot_melt_const_price, 4),
    }

    total_cost = 0
    for cost in costs.values():
        total_cost += cost

    return total_cost