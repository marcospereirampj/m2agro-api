# -*- coding: utf-8 -*-

from rest_framework import viewsets
from rest_framework import filters

from harvest.models.price_product import PriceProduct
from harvest.serializers.price_product_serializer import PriceProductSerializer


class PriceProductViewSet(viewsets.ModelViewSet):
    queryset = PriceProduct.objects.all()
    serializer_class = PriceProductSerializer
    ordering_fields = ("-creation_date",)
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter)
