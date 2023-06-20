from django.contrib import admin
from .models import Proposta, CustomFields

class CustomFieldsInline(admin.TabularInline):
    model = Proposta.campos_adicionais.through
    extra = 1

@admin.register(Proposta)
class PropostaAdmin(admin.ModelAdmin):
    inlines = [CustomFieldsInline]
    list_display = ('nome_completo', 'cpf', 'endereco', 'valor_emprestimo', 'status', 'data_proposta')
    search_fields = ['nome_completo', 'cpf']
    list_filter = ['status']

@admin.register(CustomFields)
class CustomFieldsAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo_campo')