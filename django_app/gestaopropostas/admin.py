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
            ('AN', _('Em análise')),
            ('AP', _('Aprovadas')),
            ('RE', _('Reprovadas')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'AN':
            return queryset.filter(status='AN')
        elif self.value() == 'AP':
            return queryset.filter(status='AP')
        elif self.value() == 'RE':
            return queryset.filter(status='RE')

@admin.register(Proposta)
class PropostaAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'cpf', 'endereco', 'valor_emprestimo', 'display_status', 'data_proposta')
    list_filter = (StatusFilter,)
    inlines = [CustomFieldsInline]

    def display_status(self, obj):
        return obj.get_status_display()
    display_status.short_description = 'Status'


@admin.register(CampoAdicional)
class CampoAdicionalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo_campo', 'exibir_no_formulario')