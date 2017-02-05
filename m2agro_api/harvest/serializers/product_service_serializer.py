# -*- coding: utf-8 -*-

from rest_framework import serializers

from harvest.models.product_service import ProductService


class ProductServiceSerializer(serializers.ModelSerializer):
    """


        @author Marcos Pereira
    """
    service_name = serializers.SerializerMethodField(source="get_service_name")
    product_name = serializers.SerializerMethodField(source="get_product_name")

    def get_service_name(self, obj):
        return obj.service.name

    def get_product_name(self, obj):
        return obj.product.name

    class Meta:
        model = ProductService
        fields = '__all__'
