# -*- coding: utf-8 -*-

from django.contrib import admin

from .models.harvest import Harvest
from .models.price_product import PriceProduct
from .models.product import Product
from .models.product_service import ProductService
from .models.service import Service

admin.site.register(Harvest)
admin.site.register(Product)
admin.site.register(Service)
admin.site.register(PriceProduct)
admin.site.register(ProductService)
