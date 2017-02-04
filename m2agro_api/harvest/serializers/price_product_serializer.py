# -*- coding: utf-8 -*-

from rest_framework import serializers

from harvest.models.price_product import PriceProduct


class PriceProductSerializer(serializers.ModelSerializer):
    """


        @author Marcos Pereira
    """

    class Meta:
        model = PriceProduct
        fields = '__all__'
        depth = 1
