from django.db import models

class CustomFields(models.Model):
    proposta = models.ForeignKey('Proposta', on_delete=models.CASCADE)
    campo = models.ForeignKey('CampoAdicional', on_delete=models.CASCADE)
    valor = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.proposta.nome_completo} - {self.campo.nome}"

    class Meta:
        db_table = 'custom_fields'
        verbose_name_plural = 'Custom Fields'

class CampoAdicional(models.Model):
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
        db_table = 'campo_adicional'
        verbose_name_plural = 'Campos Adicionais'

class Proposta(models.Model):
    STATUS_CHOICES = [
        ('AN', 'Em análise'),
        ('AP', 'Aprovada'),
        ('RE', 'Reprovada'),
    ]

    nome_completo = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14)
    endereco = models.CharField(max_length=200)
    valor_emprestimo = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='AN')
    data_proposta = models.DateTimeField(auto_now_add=True)
    campos_adicionais = models.ManyToManyField(CampoAdicional, through=CustomFields)

    def get_status_display(self):
        return dict(self.STATUS_CHOICES)[self.status]

    def __str__(self):
        return self.nome_completo