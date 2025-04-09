def get_total_cost(fralda, stock):
    costs = {
        'celulose_virgem': round(fralda.celulose_virgem * stock.celulose_virgem_price, 4),
        'gel': round(fralda.gel * stock.gel_price, 4),
        'tnt_filtrante_780': round(fralda.tnt_filtrante_780 * stock.tnt_filtrante_780_price, 4),
        'fita_adesiva_tape': round(fralda.fita_adesiva_tape * stock.fita_adesiva_tape_price, 4),
        'elastico_elastano_lycra': round(fralda.elastico_elastano_lycra * stock.elastico_elastano_lycra_price, 4),
        'barreira': round(fralda.barreira * stock.barreira_price, 4),
        'polietileno_filme_780': round(fralda.polietileno_filme_780 * stock.polietileno_filme_780_price, 4),
        'hot_melt_const': round(fralda.hot_melt_const * stock.hot_melt_const_price, 4),
    }

    total_cost = 0
    for cost in costs.values():
        total_cost += cost

    return total_cost