from django import forms
from .models import CustomFields

class PropostaForm(forms.Form):
    nome_completo = forms.CharField(label='Nome Completo', max_length=100)
    cpf = forms.CharField(label='CPF', max_length=14)
    endereco = forms.CharField(label='Endereço', max_length=200)
    valor_emprestimo = forms.DecimalField(label='Valor do Empréstimo Pretendido')

    # Adicione campos adicionais dinamicamente
    def __init__(self, *args, **kwargs):
        custom_fields = kwargs.pop('custom_fields', [])
        super(PropostaForm, self).__init__(*args, **kwargs)
        for field in custom_fields:
            if field.tipo_campo == 'string':
                self.fields[field.nome] = forms.CharField(label=field.nome, max_length=100)
            elif field.tipo_campo == 'number':
                self.fields[field.nome] = forms.DecimalField(label=field.nome, max_digits=100)
            elif field.tipo_campo == 'bool':
                self.fields[field.nome] = forms.BooleanField(label=field.nome, required=False)
