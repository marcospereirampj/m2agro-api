# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-04 16:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('harvest', '0005_product_weigh_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='weigh_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor Relevância(ponderador)'),
        ),
    ]