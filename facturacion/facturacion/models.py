from djongo import models

class Facturacion(models.Model):
    id_factura = models.IntegerField()
    cedula_paciente = models.IntegerField()
    objetos_factura = models.JSONField()
    costo_total = models.IntegerField()
    iva = models.IntegerField()

    def __str__(self):
        return f'Factura {self.id_factura}'


