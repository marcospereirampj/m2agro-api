# -*- coding: utf-8 -*-

from django.db import models


class Product(models.Model):
    """


        @author Marcos Pereira
    """
    name = models.CharField(verbose_name="Nome", max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'harvest'
        ordering = ['name', ]
        verbose_name = u'Produto'
        verbose_name_plural = u'Produtos'
