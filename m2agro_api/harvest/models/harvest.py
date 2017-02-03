# -*- coding: utf-8 -*-

from django.db import models


class Harvest(models.Model):
    """


        @author Marcos Pereira
    """
    name = models.CharField(verbose_name="Nome", max_length=200)
    start_date = models.DateField(verbose_name="Data de Início")
    end_date = models.DateField(verbose_name=u"Data de Término")

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'harvest'
        ordering = ['name', ]
        verbose_name = 'Safra'
        verbose_name_plural = 'Safras'