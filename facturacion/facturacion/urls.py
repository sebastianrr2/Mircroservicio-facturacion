from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^facturaciones/', views.FacturacionList, name='facturacionList'),
    url(r'^facturacioncreate/$', csrf_exempt(views.FacturacionCreate), name='facturacionCreate'),
]