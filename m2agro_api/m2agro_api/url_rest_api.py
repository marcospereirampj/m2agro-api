# -*- coding: utf-8 -*-

from django.contrib import admin
from rest_framework import routers

admin.autodiscover()

router = routers.DefaultRouter()
