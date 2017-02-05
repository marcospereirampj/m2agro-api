# -*- coding: utf-8 -*-

from rest_framework import viewsets
from rest_framework import filters

from harvest.models.product_service import ProductService
from harvest.serializers.product_service_serializer import ProductServiceSerializer


class ProductServiceViewSet(viewsets.ModelViewSet):
    queryset = ProductService.objects.all()
    serializer_class = ProductServiceSerializer
    ordering_fields = ("name",)
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter)
