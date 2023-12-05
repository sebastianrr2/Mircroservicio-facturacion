from .models import Facturacion
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
import json

def FacturacionList(request):
    queryset = Facturacion.objects.all()
    context = list(queryset.values('id', 'name'))
    return JsonResponse(context, safe=False)

def FacturacionCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        facturacion = Facturacion()
        facturacion.name = data_json["name"]
        facturacion.save()
        return HttpResponse("successfully created a facturacion")