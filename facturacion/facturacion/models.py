from django.db import models

class Facturacion(models.Model):
    paciente_id = models.CharField(max_length=100)  # Campo para almacenar el ID o información del paciente
    medico_id = models.CharField(max_length=100)    # Campo para almacenar el ID o información del médico
    fecha_emision = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    # Otros campos para la información de la factura médica.

    def __str__(self):
        return f"Factura Médica #{self.pk}"
