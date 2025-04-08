from django.db import models
from costs.models import Costs
# Create your models here.

modelos = (
    ('Bellafral', 'Bellafral'),
    ('Big Confort', 'Big Confort'),
    ('Basic Mille', 'Basic Mille'),
)

tamanhos = (
    ('XG', 'XG'),
    ('G', 'G'),
    ('M', 'M'),
)

class Bellafral(models.Model):
    modelo = models.CharField(max_length=100, choices=modelos, default='Bellafral')
    identificador = models.CharField(max_length=100)
    tamanho = models.CharField(max_length=2, choices=tamanhos)
    celulose_virgem = models.DecimalField(verbose_name='Celulose virgem (Kg)', max_digits=10, decimal_places=4, default=0)
    gel = models.DecimalField(verbose_name='Gel (Kg)', max_digits=10, decimal_places=4, default=0)
    tnt_filtrante_780 = models.DecimalField(verbose_name='TNT - Filtrante - 780mm (m2)', max_digits=10, decimal_places=4, default=0)
    fita_adesiva_tape = models.DecimalField(verbose_name='Fita adesiva - Tape (Kg)', max_digits=10, decimal_places=4, default=0)
    elastico_elastano_lycra = models.DecimalField(verbose_name='Elástico - Elastano - Lycra (Kg)', max_digits=10, decimal_places=4, default=0)
    barreira = models.DecimalField(verbose_name='Barreira (m2)', max_digits=10, decimal_places=4, default=0)
    polietileno_filme_780 = models.DecimalField(verbose_name='Polietileno - Filme - 780mm (Kg)', max_digits=10, decimal_places=4, default=0)
    hot_melt_const = models.DecimalField(verbose_name='Hot-Melt Construção (Kg)', max_digits=10, decimal_places=4, default=0)

    def __str__(self):
        return (f'{self.modelo} {self.identificador} ({self.tamanho})')

class Simulations(models.Model):
    fralda = models.JSONField(default=dict)
    fralda_object = models.ForeignKey(Bellafral, on_delete=models.CASCADE, null=True, blank=True, default=None)
    costs = models.JSONField(default=dict)
    costs_object = models.ForeignKey(Costs, on_delete=models.CASCADE, null=True, blank=True, default=None)
    simulation = models.JSONField(default=dict)

    def __str__(self):
        return (f'Fralda: {self.fralda_object} - Custo: {self.costs_object}')