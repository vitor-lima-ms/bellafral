from django.contrib import admin
from stock.models import Stock

# Register your models here.

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
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
        verbose_name = 'Stock'
        verbose_name_plural = 'Stock'