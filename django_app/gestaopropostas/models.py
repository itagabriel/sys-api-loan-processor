from django.db import models

class Proposta(models.Model):
    nome_completo = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    endereco = models.CharField(max_length=200)
    valor_emprestimo = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(default=False)
    data_proposta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_completo