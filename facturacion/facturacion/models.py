from django.db import models

class Facturacion(models.Model):
    id_factura = models.IntegerField(primary_key=True)
    cedula_paciente = models.IntegerField()
    objetos_factura = models.TextField()  # Puedes almacenar la lista de objetos como un texto, por ejemplo JSON
    costo_total = models.IntegerField()
    iva = models.IntegerField()

    def __str__(self):
        return f"Factura #{self.id_factura} - Paciente: {self.cedula_paciente}"

