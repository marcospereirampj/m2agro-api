# -*- coding: utf-8 -*-

from rest_framework import viewsets
from rest_framework import filters

from harvest.models.service import Service
from harvest.serializers.service_serializer import ServiceSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    ordering_fields = ("name",)
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter)
