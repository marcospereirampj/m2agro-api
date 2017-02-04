# -*- coding: utf-8 -*-

from rest_framework import serializers

from harvest.models.harvest import Harvest


class HarvestSerializer(serializers.ModelSerializer):
    """


        @author Marcos Pereira
    """

    class Meta:
        model = Harvest
        fields = '__all__'
