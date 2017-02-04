# -*- coding: utf-8 -*-

from rest_framework import serializers

from harvest.models.product import Product


class ProductSerializer(serializers.ModelSerializer):
    """


        @author Marcos Pereira
    """

    class Meta:
        model = Product
        fields = '__all__'
