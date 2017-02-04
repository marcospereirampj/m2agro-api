# -*- coding: utf-8 -*-

from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from harvest.forms.price_product_form import PriceProductForm
from harvest.serializers.price_product_serializer import PriceProductSerializer


class PriceProductViewSet(APIView):
    """


        @author Marcos Pereira
    """
    def post(self, request):
        data = request.data
        price_product_form = PriceProductForm(data)

        if price_product_form.is_valid():
            price_product = price_product_form.save(commit=True)
            price_product_serializer = PriceProductSerializer(price_product)

            return Response(price_product_serializer.data, status=HTTP_201_CREATED)

        return Response(price_product_form.errors, status=HTTP_400_BAD_REQUEST)
