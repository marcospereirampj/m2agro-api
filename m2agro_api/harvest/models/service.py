# -*- coding: utf-8 -*-

from django.db import models

from harvest.models.harvest import Harvest


class Service(models.Model):
    """


        @author Marcos Pereira
    """
    name = models.CharField(verbose_name="Nome", max_length=200)
    start_date = models.DateField(verbose_name="Data de Início")
    end_date = models.DateField(verbose_name=u"Data de Término")
    harvest = models.ForeignKey(Harvest, verbose_name=u"Safra")
    cost = models.DecimalField(verbose_name=u"Custo Total",
                               max_digits=13, decimal_places=3)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'harvest'
        ordering = ['name', ]
        verbose_name = u'Serviço'
        verbose_name_plural = u'Serviços'