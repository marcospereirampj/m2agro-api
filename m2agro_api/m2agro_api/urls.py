# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from rest_framework import routers

from harvest.rest_api.harvest_viewset import HarvestViewSet
from harvest.rest_api.price_product_viewset import PriceProductViewSet
from harvest.rest_api.product_service_viewset import ProductServiceViewSet
from harvest.rest_api.update_products_viewset import UpdateProductsViewSet
from harvest.rest_api.product_viewset import ProductViewSet
from harvest.rest_api.service_viewset import ServiceViewSet

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'harvest', HarvestViewSet)
router.register(r'product', ProductViewSet)
router.register(r'service', ServiceViewSet)
router.register(r'product-service', ProductServiceViewSet)
router.register(r'price-product', PriceProductViewSet)


urlpatterns = [
    url(r'^manager/', include(admin.site.urls)),

    url(r'^api/update_products/$', UpdateProductsViewSet.as_view()),

    url(r'^api/', include(router.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
