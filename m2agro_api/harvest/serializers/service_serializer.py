# -*- coding: utf-8 -*-

from rest_framework import serializers

from harvest.models.service import Service


class ServiceSerializer(serializers.ModelSerializer):
    """


        @author Marcos Pereira
    """

    class Meta:
        model = Service
        fields = '__all__'
        depth = 1
