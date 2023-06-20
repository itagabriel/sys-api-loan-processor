from django.shortcuts import render, redirect
from .forms import PropostaForm
from .models import CustomFields, Proposta, CampoAdicional
from .serializers import PropostaSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

def index(request):
    form = PropostaForm()
    campos_adicionais = CampoAdicional.objects.filter(exibir_no_formulario=True)
    return render(
        request,
        'gestaopropostas/index.html',
        {'form': form, 'campos_adicionais': campos_adicionais}
    )

@api_view(['POST'])
def criar_proposta(request):
    if request.method == 'POST':
        form = PropostaForm(request.POST)
        if form.is_valid():
            nome_completo = form.cleaned_data['nome_completo']
            cpf = form.cleaned_data['cpf']
            endereco = form.cleaned_data['endereco']
            valor_emprestimo = form.cleaned_data['valor_emprestimo']

            # Salvar os dados do formulário no objeto Proposta
            proposta = Proposta(nome_completo=nome_completo, cpf=cpf, endereco=endereco, valor_emprestimo=valor_emprestimo)
            proposta.save()

            # Salvar os campos customizados
            campos_adicionais = CampoAdicional.objects.filter(exibir_no_formulario=True)
            for campo_adicional in campos_adicionais:
                valor = request.POST.get(f'custom_field_{campo_adicional.id}')
                if valor:
                    campo_customizado = CustomFields(proposta=proposta, campo=campo_adicional, valor=valor)
                    campo_customizado.save()

            # Redirecionar para a página de sucesso
            return redirect('/sucesso/')
    else:
        form = PropostaForm()

    campos_adicionais = CampoAdicional.objects.filter(exibir_no_formulario=True)
    return render(request, 'gestaopropostas/criar_proposta.html', {'form': form, 'campos_adicionais': campos_adicionais})

    # Obtenha todos os campos adicionais disponíveis
    campos_adicionais = CampoAdicional.objects.filter(exibir_no_formulario=True)

    return render(request, 'gestaopropostas/criar_proposta.html', {'form': form, 'campos_adicionais': campos_adicionais})

def sucesso(request):
    return render(request, 'gestaopropostas/sucesso.html')

