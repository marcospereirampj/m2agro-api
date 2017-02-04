# -*- coding: utf-8 -*-
import datetime

from django.db.models.aggregates import Sum
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from rest_framework.views import APIView

from harvest.models.price_product import PriceProduct
from harvest.models.product import Product
from harvest.models.product_service import ProductService
from harvest.models.service import Service
from harvest.serializers.product_serializer import ProductSerializer


class UpdateProductsViewSet(APIView):
    """


        @author Marcos Pereira
    """

    def post(self, request):
        current_month, current_year = datetime.datetime.today().month, datetime.datetime.today().year
        month, year = (current_month-1, current_year) if current_month-1 > 0 else (12, current_year-1)
        services = Service.objects.filter(start_date__month=month, start_date__year=year)

        if services:
            # Sum of amount by product
            products_amount = ProductService.objects\
                .filter(service__in=services)\
                .values('product')\
                .annotate(amount_total=Sum('amount'))

            # Sum of services from previous month
            cost_services = services.aggregate(value_total=Sum('cost'))

            # update history of products prices
            for p in products_amount:
                product = get_object_or_404(Product, pk=p['product'])
                price_product = PriceProduct()
                price_product.product = product

                # Attention for product.weigh_price (is ponder)
                price_product.average_price = \
                    (cost_services['value_total']/p['amount_total'])*product.weigh_price

                price_product.save()

            # Return products list updated
            products = Product.objects.all()
            products_serializer = ProductSerializer(products, many=True)

            return Response(products_serializer.data, status=HTTP_200_OK)
        else:
            return Response({'Services not found'}, status=HTTP_400_BAD_REQUEST)