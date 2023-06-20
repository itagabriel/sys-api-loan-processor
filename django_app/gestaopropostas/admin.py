from django.contrib import admin
from .models import Proposta, CampoAdicional, CustomFields
from django.utils.translation import gettext_lazy as _
class CustomFieldsInline(admin.TabularInline):
    model = CustomFields
    extra = 0
    verbose_name_plural = 'Campos Adicionais'



class StatusFilter(admin.SimpleListFilter):
    title = _('Status')
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return (
            ('sim', _('Aprovadas')),
            ('nao', _('Reprovadas')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'sim':
            return queryset.filter(status=True)
        if self.value() == 'nao':
            return queryset.filter(status=False)

@admin.register(Proposta)
class PropostaAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'cpf', 'endereco', 'valor_emprestimo', 'get_status_display', 'data_proposta')
    list_filter = (StatusFilter,)
    inlines = [CustomFieldsInline]

    def get_status_display(self, obj):
        if obj.status:
            return 'Aprovada'
        else:
            return 'Reprovada'
    get_status_display.short_description = 'Status'



@admin.register(CampoAdicional)
class CampoAdicionalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo_campo', 'exibir_no_formulario')

