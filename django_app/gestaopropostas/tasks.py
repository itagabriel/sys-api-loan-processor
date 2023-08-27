from celery import shared_task
from django.apps import apps
import requests

@shared_task
def avaliar_proposta(proposta_id):
    Proposta = apps.get_model('gestaopropostas', 'Proposta')
    proposta = Proposta.objects.get(id=proposta_id)
    
    # Definindo a URL base da API de Análise de Crédito
    api_url = "https://loan-processor.digitalsys.com.br/api/v1"

    # Endpoint específico para avaliação de empréstimo
    loan_endpoint = "/loan/"

    # Preparando os dados da proposta para serem enviados à API
    payload = {
        "document": proposta.cpf,      # CPF do solicitante
        "name": proposta.nome_completo # Nome do solicitante
    }

    try:
        # Realizando a chamada à API para avaliação de crédito
        response = requests.post(api_url + loan_endpoint, json=payload)
        response_data = response.json()

        if response.status_code == 200 and response_data.get("approved"):
            proposta.status = 'AN'  # Atualiza o status da proposta para "Análise" (para que o administrador django consiga analisar a proposta)
            proposta.save()
            print("Proposta aprovada e enviada para análise do administrador")
        else:
            proposta.status = 'RE'  # Atualiza o status da proposta para "Reprovada"
            proposta.save()
            print("Proposta negada")
    except requests.exceptions.RequestException as e:
        print("Erro durante a chamada à API:", str(e))