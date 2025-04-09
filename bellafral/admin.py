from django.contrib import admin
from bellafral.models import Bellafral, Simulations

# Register your models here.

@admin.register(Bellafral)
class BellafralAdmin(admin.ModelAdmin):
    list_display = (
        'modelo',
        'identificador',
        'tamanho',
        'celulose_virgem',
        'gel',
        'tnt_filtrante_780',
        'fita_adesiva_tape',
        'elastico_elastano_lycra',
        'barreira',
        'polietileno_filme_780',
        'hot_melt_const',
    )

    class Meta:
        verbose_name_plural = 'Bellafral'

@admin.register(Simulations)
class SimulationsAdmin(admin.ModelAdmin):
    list_display = ('fralda_object', 'costs_object')

    class Meta:
        verbose_name_plural = 'Simulations'