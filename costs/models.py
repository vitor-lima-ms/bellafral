from django.db import models

# Create your models here.

class Costs(models.Model):
    identificador = models.CharField(max_length=100, default='')
    celulose_virgem_price = models.DecimalField(verbose_name='Celulose virgem (R$)', max_digits=10, decimal_places=4, default=0)
    gel_price = models.DecimalField(verbose_name='Gel (R$)', max_digits=10, decimal_places=4, default=0)
    tnt_filtrante_780_price = models.DecimalField(verbose_name='TNT - filtrante 780mm (R$)', max_digits=10, decimal_places=4, default=0)
    fita_adesiva_tape_price = models.DecimalField(verbose_name='Fita adesiva - Tape (R$)', max_digits=10, decimal_places=4, default=0)
    elastico_elastano_lycra_price = models.DecimalField(verbose_name='Elástico - Elastano - Lycra (R$)', max_digits=10, decimal_places=4, default=0)
    barreira_price = models.DecimalField(verbose_name='Barreira (R$)', max_digits=10, decimal_places=4, default=0)
    polietileno_filme_780_price = models.DecimalField(verbose_name='Polietileno - Filme - 780mm (R$)', max_digits=10, decimal_places=4, default=0)
    hot_melt_const_price = models.DecimalField(verbose_name='Hot-Melt Construção (R$)', max_digits=10, decimal_places=4, default=0)

    def __str__(self):
        return self.identificador
