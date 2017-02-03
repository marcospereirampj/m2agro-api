# -*- coding: utf-8 -*-

from django.db import models

from harvest.models.product import Product
from harvest.models.service import Service


class ProductService(models.Model):
    """


        @author Marcos Pereira
    """
    service = models.ForeignKey(Service, verbose_name=u"Serviço")
    product = models.ForeignKey(Product, verbose_name=u"Produto")
    amount = models.DecimalField(verbose_name=u"Quantidade",
                                 decimal_places=3, max_digits=12)

    def __str__(self):
        return "%s - %s" % (self.product.name, self.amount)

    class Meta:
        app_label = 'harvest'
        ordering = ['amount', ]
        verbose_name = 'Produto do Serviço'
        verbose_name_plural = 'Produtos do Serviço'
