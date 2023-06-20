from django.db import models

class CustomFields(models.Model):
    TIPO_CAMPO_CHOICES = [
        ('string', 'Texto'),
        ('number', 'Numérico'),
        ('bool', 'Booleano'),
    ]

    nome = models.CharField(max_length=100)
    tipo_campo = models.CharField(max_length=6, choices=TIPO_CAMPO_CHOICES)
    exibir_no_formulario = models.BooleanField(default=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        db_table = 'custom_fields'
        verbose_name_plural = 'Custom Fields'

    
class Proposta(models.Model):
    campos_adicionais = models.ManyToManyField(CustomFields)
    nome_completo = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14)
    endereco = models.CharField(max_length=200)
    valor_emprestimo = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=False)
    data_proposta = models.DateTimeField(auto_now_add=True)

    def get_status_display(self):
        if self.status:
            return "Aprovada"
        else:
            return "Negada"

    def __str__(self):
        return self.nome_completo