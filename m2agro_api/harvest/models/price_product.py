# -*- coding: utf-8 -*-

from django.db import models

from harvest.models.product import Product


class PriceProduct(models.Model):
    """


        @author Marcos Pereira
    """
    product = models.ForeignKey(Product, verbose_name=u"Produto")
    average_price = models.DecimalField(verbose_name=u"Preço Médio",
                                        decimal_places=3, max_digits=12)
    creation_date = models.DateField(verbose_name="Data de Criação",
                                     auto_created=True,
                                     auto_now_add=True)

    def save(self, *args, **kwargs):
        super(PriceProduct, self).save(*args, **kwargs)
        self.product.last_average_price = self.average_price
        self.product.save()

    def __str__(self):
        return "%s - %s - %s" % (self.product.name, self.average_price, self.creation_date)

    class Meta:
        app_label = 'harvest'
        ordering = ['-creation_date', ]
        verbose_name = u'Preço Médio'
        verbose_name_plural = u'Preços Médio'
