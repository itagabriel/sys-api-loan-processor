from django.shortcuts import render, redirect
from .forms import PropostaForm
from .models import CustomFields
from .serializers import PropostaSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

def index(request):
    form = PropostaForm()
    custom_fields = CustomFields.objects.filter(exibir_no_formulario=True)
    return render(
        request,
        'gestaopropostas/index.html',
        {'form': form, 'custom_fields': custom_fields}
    )

@api_view(['POST'])
def criar_proposta(request):
    if request.method == 'POST':
        form = PropostaForm(request.POST)
        if form.is_valid():
            proposta = form.save()
            serializer = PropostaSerializer(proposta)
            return Response(serializer.data, status=201)
    
    return Response(status=400)

@api_view(['GET'])
def sucesso(request):
    return render(request, 'gestaopropostas/sucesso.html')