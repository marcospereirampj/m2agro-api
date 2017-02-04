# -*- coding: utf-8 -*-

from rest_framework import viewsets
from rest_framework import filters

from harvest.models.product import Product
from harvest.serializers.product_serializer import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    ordering_fields = ("name",)
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter)
