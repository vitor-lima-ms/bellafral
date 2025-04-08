from django.db import models

# Create your models here.

tamanhos = (
    ('XG', 'XG'),
    ('G', 'G'),
    ('M', 'M'),
)

class Bellafral(models.Model):
    nome = models.CharField(max_length=100)
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
        return (f'{self.nome} ({self.tamanho})')

class Simulations(models.Model):
    fralda = models.JSONField(default=dict)
    stock = models.JSONField(default=dict)
    simulation = models.JSONField(default=dict)