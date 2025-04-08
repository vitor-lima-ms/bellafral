from django.contrib import admin
from costs.models import Costs

# Register your models here.

@admin.register(Costs)
class CostsAdmin(admin.ModelAdmin):
    list_display = (
        'celulose_virgem_price',
        'gel_price',
        'tnt_filtrante_780_price',
        'fita_adesiva_tape_price',
        'elastico_elastano_lycra_price',
        'barreira_price',
        'polietileno_filme_780_price',
        'hot_melt_const_price',
    )

    class Meta:
        verbose_name = 'Cost'
        verbose_name_plural = 'Costs'