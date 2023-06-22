from celery import shared_task
from django.apps import apps

@shared_task
def avaliar_proposta(proposta_id):
    Proposta = apps.get_model('gestaopropostas', 'Proposta')
    proposta = Proposta.objects.get(id=proposta_id)
    
    # Verificar se o ID da proposta é par ou ímpar
    if proposta_id % 2 == 0:
        proposta.status = 'AP'  # Aprovado para IDs pares
        proposta.save()
    else:
        proposta.status = 'RE'  # Reprovado para IDs ímpares
        proposta.save()

    return proposta.status