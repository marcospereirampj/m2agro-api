# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-04 03:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('harvest', '0002_auto_20170203_2009'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name'], 'verbose_name': 'Produto', 'verbose_name_plural': 'Produtos'},
        ),
        migrations.AddField(
            model_name='product',
            name='last_average_price',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=12, verbose_name='Último Preço Médio'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productservice',
            name='amount',
            field=models.DecimalField(decimal_places=3, max_digits=12, verbose_name='Quantidade'),
        ),
    ]