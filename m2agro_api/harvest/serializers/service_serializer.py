# -*- coding: utf-8 -*-

from rest_framework import serializers

from harvest.models.service import Service


class ServiceSerializer(serializers.ModelSerializer):
    """


        @author Marcos Pereira
    """
    harvest_name = serializers.SerializerMethodField(source="get_harvest_name")

    def get_harvest_name(self, obj):
        return obj.harvest.name

    class Meta:
        model = Service
        fields = '__all__'
