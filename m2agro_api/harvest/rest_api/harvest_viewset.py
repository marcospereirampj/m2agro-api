# -*- coding: utf-8 -*-

from rest_framework import viewsets
from rest_framework import filters

from harvest.models.harvest import Harvest
from harvest.serializers.harvest_serializer import HarvestSerializer


class HarvestViewSet(viewsets.ModelViewSet):
    queryset = Harvest.objects.all()
    serializer_class = HarvestSerializer
    ordering_fields = ("name",)
    filter_backends = (filters.DjangoFilterBackend, filters.OrderingFilter)
