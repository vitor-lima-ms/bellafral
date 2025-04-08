from django.db import models

# Create your models here.

class Costs(models.Model):
    nome = models.CharField(max_length=100, default='')
    celulose_virgem_price = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    gel_price = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    tnt_filtrante_780_price = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    fita_adesiva_tape_price = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    elastico_elastano_lycra_price = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    barreira_price = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    polietileno_filme_780_price = models.DecimalField(max_digits=10, decimal_places=4, default=0)
    hot_melt_const_price = models.DecimalField(max_digits=10, decimal_places=4, default=0)

    def __str__(self):
        return self.nome
