from django.contrib import admin
from .models import Proposta

@admin.register(Proposta)
class PropostaAdmin(admin.ModelAdmin):
    list_display = ['nome_completo', 'cpf', 'endereco', 'valor_emprestimo', 'status', 'data_proposta']
    search_fields = ['nome_completo', 'cpf']
    list_filter = ['status']