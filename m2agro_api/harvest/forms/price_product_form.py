
# -*- coding: utf-8 -*-

from django import forms

from harvest.models.price_product import PriceProduct


class PriceProductForm(forms.ModelForm):
    """


        @author Marcos Pereira
    """
    class Meta:
        model = PriceProduct
        fields = '__all__'
        exclude = ('creation_date',)
