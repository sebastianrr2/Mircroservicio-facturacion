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
        data = json.loads(request.body)
        
        id_factura = data.get("id", None)
        cedula_paciente = data.get("cedulapaciente", None)
        objetos_factura = data.get("objetosfactura", [])
        costo_total = data.get("costototal", None)
        iva = data.get("iva", None)

        if id_factura is not None and cedula_paciente is not None and costo_total is not None and iva is not None:
            facturacion = Facturacion(
                id=id_factura,
                cedulapaciente=cedula_paciente,
                objetosfactura=objetos_factura,
                costototal=costo_total,
                iva=iva
            )
            facturacion.save()
            return HttpResponse("Facturacion created successfully")
        else:
            return HttpResponse("Some required fields are missing", status=400)
    else:
        return HttpResponse("Invalid request method", status=405)