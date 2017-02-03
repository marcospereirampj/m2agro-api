# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from .url_rest_api import router

admin.autodiscover()


urlpatterns = [
    url(r'^manager/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
