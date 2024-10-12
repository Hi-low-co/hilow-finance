from django.db import models

# Create your models here.

## Table de Contas
class FinancialRecord(models.Model):
    DT_VENCIMENTO = models.DateField()  # Data de vencimento
    TP_CONTA = models.CharField(max_length=10,null=True)
    DS_CONTA = models.CharField(max_length=255)  # Descrição da conta
    DS_PERIODO_REFERENCIA = models.CharField(max_length=100)  # Período de referência
    NU_VALOR = models.FloatField(null=True)   
    DT_PAGAMENTO = models.DateField(null=True, blank=True)  # Data de pagamento (pode ser opcional)

    def __str__(self):
        return f'{self.DS_CONTA} - {self.DS_PERIODO_REFERENCIA}'