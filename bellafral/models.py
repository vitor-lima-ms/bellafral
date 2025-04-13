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
    identificador = models.CharField(verbose_name='Identificador', max_length=100)
    tamanho = models.CharField(max_length=2, choices=tamanhos)
    
    celulose_virgem = models.DecimalField(verbose_name='Celulose virgem (Kg)', max_digits=10, decimal_places=4, default=0)
    celulose_virgem_total_unit_cost = models.DecimalField(verbose_name='Custo unitário da celulose virgem (R$)', max_digits=10, decimal_places=4, default=0, blank=True, null=True)
    
    gel = models.DecimalField(verbose_name='Gel (Kg)', max_digits=10, decimal_places=4, default=0)
    gel_total_unit_cost = models.DecimalField(verbose_name='Custo unitário do gel (R$)', max_digits=10, decimal_places=4, default=0, blank=True, null=True)
    
    tnt_filtrante_780 = models.DecimalField(verbose_name='TNT - Filtrante - 780mm (m2)', max_digits=10, decimal_places=4, default=0)
    tnt_filtrante_780_total_unit_cost = models.DecimalField(verbose_name='Custo unitário do TNT - Filtrante - 780mm (R$)', max_digits=10, decimal_places=4, default=0, blank=True, null=True)
    
    fita_adesiva_tape = models.DecimalField(verbose_name='Fita adesiva - Tape (Kg)', max_digits=10, decimal_places=4, default=0)
    fita_adesiva_tape_total_unit_cost = models.DecimalField(verbose_name='Custo unitário da fita adesiva - Tape (R$)', max_digits=10, decimal_places=4, default=0, blank=True, null=True)
    
    elastico_elastano_lycra = models.DecimalField(verbose_name='Elástico - Elastano - Lycra (Kg)', max_digits=10, decimal_places=4, default=0)
    elastico_elastano_lycra_total_unit_cost = models.DecimalField(verbose_name='Custo unitário do elástico - Elastano - Lycra (R$)', max_digits=10, decimal_places=4, default=0, blank=True, null=True)
    
    barreira = models.DecimalField(verbose_name='Barreira (m2)', max_digits=10, decimal_places=4, default=0)
    barreira_total_unit_cost = models.DecimalField(verbose_name='Custo unitário da barreira (R$)', max_digits=10, decimal_places=4, default=0, blank=True, null=True)
    
    polietileno_filme_780 = models.DecimalField(verbose_name='Polietileno - Filme - 780mm (Kg)', max_digits=10, decimal_places=4, default=0)
    polietileno_filme_780_total_unit_cost = models.DecimalField(verbose_name='Custo unitário do polietileno - Filme - 780mm (R$)', max_digits=10, decimal_places=4, default=0, blank=True, null=True)
    
    hot_melt_const = models.DecimalField(verbose_name='Hot-Melt Construção (Kg)', max_digits=10, decimal_places=4, default=0)
    hot_melt_const_total_unit_cost = models.DecimalField(verbose_name='Custo unitário do Hot-Melt Construção (R$)', max_digits=10, decimal_places=4, default=0, blank=True, null=True)

    total_cost = models.DecimalField(verbose_name='Custo total (R$)', max_digits=10, decimal_places=4, default=0, blank=True, null=True)

    loss_percentage = models.DecimalField(verbose_name='Perdas (%)', max_digits=10, decimal_places=4, default=0)

    total_cost_with_loss = models.DecimalField(verbose_name='Custo total com perdas (R$)', max_digits=10, decimal_places=4, default=0, blank=True, null=True)

    qtd_p_pacote = models.IntegerField(verbose_name='Quantidade de peças por pacote', default=0)

    embalagem = models.DecimalField(verbose_name='Embalagem (R$)', max_digits=10, decimal_places=4, default=0)

    saco_fardos = models.DecimalField(verbose_name='Saco para fardos/Encarte (R$)', max_digits=10, decimal_places=4, default=0)

    custo_pacote = models.DecimalField(blank=True, null=True, verbose_name='Custo do pacote (R$)', max_digits=10, decimal_places=4, default=0)

    custo_unitario_final = models.DecimalField(blank=True, null=True, verbose_name='Custo unitário final (R$)', max_digits=10, decimal_places=4, default=0)

    comissao = models.DecimalField(verbose_name='Comissão (%)', max_digits=10, decimal_places=4, default=0)

    impostos = models.DecimalField(verbose_name='Impostos (%)', max_digits=10, decimal_places=4, default=0)

    frete = models.DecimalField(verbose_name='Frete (%)', max_digits=10, decimal_places=4, default=0)

    margem_contribuicao = models.DecimalField(verbose_name='Margem de contribuição (%)', max_digits=10, decimal_places=4, default=0)

    st = models.DecimalField(verbose_name='ST (%)', max_digits=10, decimal_places=4, default=0)

    preco_venda = models.DecimalField(blank=True, null=True, verbose_name='Preço de venda (R$)', max_digits=10, decimal_places=4, default=0)

    preco_venda_unitario = models.DecimalField(blank=True, null=True, verbose_name='Preço de venda unitário (R$)', max_digits=10, decimal_places=4, default=0)

    preco_venda_st = models.DecimalField(blank=True, null=True, verbose_name='Preço de venda com ST (R$)', max_digits=10, decimal_places=4, default=0)

    preco_venda_st_unitario = models.DecimalField(blank=True, null=True, verbose_name='Preço de venda unitário com ST (R$)', max_digits=10, decimal_places=4, default=0)

    def __str__(self):
        return (f'{self.modelo} {self.identificador} ({self.tamanho})')

class Simulations(models.Model):
    fralda_object = models.ForeignKey(Bellafral, on_delete=models.CASCADE, null=True, blank=True, default=None)
    costs_object = models.ForeignKey(Costs, on_delete=models.CASCADE, null=True, blank=True, default=None)

    def __str__(self):
        return (f'Fralda: {self.fralda_object} - Custo: {self.costs_object}')