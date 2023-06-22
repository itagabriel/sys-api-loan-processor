from django import forms
from django.test import TestCase
from .forms import PropostaForm
class PropostaFormTest(TestCase):
    def test_nome_completo_field(self):
        form = PropostaForm()
        self.assertTrue(form.fields['nome_completo'].required)
        self.assertEqual(form.fields['nome_completo'].label, 'Nome Completo')

    def test_cpf_field(self):
        form = PropostaForm()
        self.assertTrue(form.fields['cpf'].required)
        self.assertEqual(form.fields['cpf'].label, 'CPF')

    def test_endereco_field(self):
        form = PropostaForm()
        self.assertTrue(form.fields['endereco'].required)
        self.assertEqual(form.fields['endereco'].label, 'Endereço')
        self.assertEqual(form.fields['endereco'].max_length, 200)

    def test_valor_emprestimo_field(self):
        form = PropostaForm()
        self.assertTrue(form.fields['valor_emprestimo'].required)
        self.assertEqual(form.fields['valor_emprestimo'].label, 'Valor do Empréstimo Pretendido')
        self.assertIsInstance(form.fields['valor_emprestimo'], forms.DecimalField)