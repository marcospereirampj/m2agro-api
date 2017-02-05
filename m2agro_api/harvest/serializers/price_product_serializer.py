# -*- coding: utf-8 -*-

from rest_framework import serializers

from harvest.models.price_product import PriceProduct


class PriceProductSerializer(serializers.ModelSerializer):
    """


        @author Marcos Pereira
    """

    product_name = serializers.SerializerMethodField(source="get_product_name")

    def get_product_name(self, obj):
        return obj.product.name

    class Meta:
        model = PriceProduct
        fields = '__all__'
